from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, timedelta
import calendar


def create_calendar(year=None, month=None):
    now = datetime.now()
    if year is None:
        year = now.year
    if month is None:
        month = now.month

    today_day = now.day if (year == now.year and month == now.month) else None

    keyboard = []

    row = [
        InlineKeyboardButton(
            text=f"{calendar.month_name[month]} {year}",
            callback_data="ignore"
        )
    ]
    keyboard.append(row)
    row = [InlineKeyboardButton(day, callback_data="ignore") for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]]
    keyboard.append(row)
    my_calendar = calendar.monthcalendar(year, month)
    for week in my_calendar:
        row = []
        for day in week:
            if day == 0:  
                row.append(InlineKeyboardButton(" ", callback_data="ignore"))
            else:
                day_text = f"🔹{day}" if day == today_day else str(day)
                row.append(
                    InlineKeyboardButton(
                        text=day_text,
                        callback_data=f"select_{year}-{month:02d}-{day:02d}"
                    )
                )
        keyboard.append(row)

    previous_month = datetime(year, month, 1) - timedelta(days=1)
    next_month = datetime(year, month, 28) + timedelta(days=4)
    next_month = next_month.replace(day=1)

    row = [
        InlineKeyboardButton("<", callback_data=f"prev:{previous_month.year}-{previous_month.month}"),
        InlineKeyboardButton(" ", callback_data="ignore"),
        InlineKeyboardButton(">", callback_data=f"next:{next_month.year}-{next_month.month}"),
    ]
    keyboard.append(row)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
