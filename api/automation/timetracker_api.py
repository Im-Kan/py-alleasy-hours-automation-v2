import requests
from datetime import datetime


class TimetrackerAPI:
    """7pace Timetracker Reporting API v3 client."""

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json',
        }

    def get_worklogs_work_items(self, year: int, month: int) -> list:
        """
        Fetches worklogs with linked work item data for a given month.
        Uses prefilter=Me to get only the authenticated user's data.
        PeriodLength is in seconds.
        """
        start = datetime(year, month, 1).strftime('%Y-%m-%dT00:00:00Z')
        if month == 12:
            end = datetime(year + 1, 1, 1).strftime('%Y-%m-%dT00:00:00Z')
        else:
            end = datetime(year, month + 1, 1).strftime('%Y-%m-%dT00:00:00Z')

        params = (
            f"$filter=Timestamp ge {start} and Timestamp lt {end}"
            f"&$orderby=Timestamp asc"
            f"&prefilter=Me"
        )

        url = f"{self.base_url}/workLogsWorkItems?{params}"

        all_results = []
        while url:
            resp = requests.get(url, headers=self.headers, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            all_results.extend(data.get('value', []))
            url = data.get('@odata.nextLink')
        return all_results

    def to_rows(self, worklogs: list) -> list:
        """
        Transforms API response into dicts matching the columns
        that time_explorer.py expects: date, title, work_item_type,
        comment, activity_type, hours.
        """
        rows = []
        for wl in worklogs:
            worklog_date = wl.get('WorklogDate', {})
            work_item = wl.get('WorkItem', {})
            activity = wl.get('ActivityType', {})

            date_val = worklog_date.get('ShortDate', '')
            if not date_val:
                ts = wl.get('Timestamp', '')
                if ts:
                    date_val = ts[:10]

            rows.append({
                'date': date_val,
                'title': work_item.get('System_Title', ''),
                'work_item_type': work_item.get('System_WorkItemType', ''),
                'comment': wl.get('Comment', '') or '',
                'activity_type': activity.get('Name', '') if isinstance(activity, dict) else str(activity or ''),
                'hours': wl.get('PeriodLength', 0) / 3600,
            })
        return rows
