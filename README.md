# Telegram Bot Inline Calendar 📅  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  

This repository provides a **simple inline calendar** for Telegram bots built with [Aiogram](https://docs.aiogram.dev). It allows users to select dates easily and includes features like **blocking past dates** and **month navigation**.  

---

## ✨ Features  

- **User-Friendly Interface**: Displays an inline calendar for date selection.  
- **Date Validation**: Prevents users from selecting past dates with a helpful alert.  
- **Interactive Navigation**: Navigate through months using "Previous" and "Next" buttons.  
- **Current Date Highlight**: Marks the current day with a special icon for clarity.  

---

## 🚀 Getting Started  

### Prerequisites  

Ensure you have the following installed:  

- Python 3.8+  
- Aiogram 3.x  
- A configured Telegram Bot Token from [BotFather](https://t.me/BotFather).  

---

## 📖 Usage  

### Example Handler  

Add the following handler to your bot to allow users to create a trip and select a date:  

```python
@dp.message_handler(lambda message: message.text == "Створити поїздку")
async def my_parcel(message: types.Message):
    await message.answer(
        "<b>Оберіть дату поїздки:</b>", 
        parse_mode="HTML", 
        reply_markup=create_calendar()
    )



**##** Demo video
