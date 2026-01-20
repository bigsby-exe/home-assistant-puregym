"""PureGym API Client."""
import logging
import aiohttp

TIMEOUT = 10

_LOGGER: logging.Logger = logging.getLogger(__package__)


class PuregymAttendanceApiClient:
    """PureGym Attendance API Client."""
    def __init__(
        self, username: str, password: str, session: aiohttp.ClientSession
    ) -> None:
        """Initialize PureGym API Client."""
        self._username = username
        self._password = password
        self._session = session

    async def async_get_data(self) -> dict:
        """Get attendance data from PureGym API."""
        authed = False
        access_token = None
        home_gym_id = None
        
        # Authenticate and get access token
        auth_headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'PureGym/1523 CFNetwork/1312 Darwin/21.0.0'
        }
        data = {
            'grant_type': 'password',
            'username': self._username,
            'password': self._password,
            'scope': 'pgcapi',
            'client_id': 'ro.client'
        }

        try:
            async with self._session.post(
                'https://auth.puregym.com/connect/token',
                headers=auth_headers,
                data=data,
                timeout=aiohttp.ClientTimeout(total=TIMEOUT)
            ) as response:
                if response.status == 200:
                    auth_json = await response.json()
                    authed = True
                    access_token = auth_json.get('access_token')
                else:
                    error_text = await response.text()
                    _LOGGER.error(
                        "Authentication failed with status %s: %s",
                        response.status,
                        error_text
                    )

            if not authed or not access_token:
                _LOGGER.error("Permission Error: Failed to authenticate")
                raise Exception("Authentication failed")

            # Prepare headers for API requests (GET requests shouldn't have Content-Type)
            api_headers = {
                'Authorization': 'Bearer ' + access_token,
                'User-Agent': 'PureGym/1523 CFNetwork/1312 Darwin/21.0.0'
            }

            # Get member info to find home gym ID
            async with self._session.get(
                'https://capi.puregym.com/api/v1/member',
                headers=api_headers,
                timeout=aiohttp.ClientTimeout(total=TIMEOUT)
            ) as response:
                if response.status == 200:
                    member_json = await response.json()
                    home_gym_id = member_json.get('homeGymId')
                else:
                    error_text = await response.text()
                    _LOGGER.error(
                        'Failed to get member info: status %s, %s',
                        response.status,
                        error_text
                    )
                    raise Exception(f"Failed to get member info: {response.status}")

            if not home_gym_id:
                _LOGGER.error("No home gym ID found")
                raise Exception("No home gym ID found")

            # Get attendance data
            async with self._session.get(
                f'https://capi.puregym.com/api/v1/gyms/{str(home_gym_id)}/attendance',
                headers=api_headers,
                timeout=aiohttp.ClientTimeout(total=TIMEOUT)
            ) as response:
                if response.status == 200:
                    attendance_json = await response.json()
                    total_people = attendance_json.get('totalPeopleInGym', 0)
                    return {"totalPeopleInGym": total_people}
                else:
                    error_text = await response.text()
                    _LOGGER.error(
                        'Failed to get attendance: status %s, %s',
                        response.status,
                        error_text
                    )
                    raise Exception(f"Failed to get attendance: {response.status}")

        except aiohttp.ClientError as exception:
            _LOGGER.error("Error fetching information from PureGym API: %s", exception)
            raise
        except Exception as exception:
            _LOGGER.error("Unexpected error: %s", exception)
            raise
