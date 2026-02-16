# OpenLibrary Books Project

این پروژه با **Python** اطلاعات کتاب‌ها را از **OpenLibrary API** دریافت می‌کند و کتاب‌هایی که بعد از سال ۲۰۰۰ منتشر شده‌اند را در یک فایل CSV ذخیره می‌کند.

---

## ویژگی‌ها

- دریافت کتاب‌ها با API رسمی OpenLibrary  
- فیلتر کتاب‌هایی که بعد از سال ۲۰۰۰ منتشر شده‌اند  
- مرتب‌سازی بر اساس سال انتشار  
- ذخیره خروجی در فایل CSV  

---

## پیش‌نیازها

- Python 3.x  
- کتابخانه `requests`

نصب کتابخانه:

```bash
pip install requests
نحوه اجرا
فایل پروژه را دانلود یا clone کن:

git clone https://github.com/username/openlibrary-books.git
cd openlibrary-books
اسکریپت را اجرا کن:

python main.py
پس از اجرا، فایل خروجی CSV با نام books_after_2000.csv ساخته می‌شود و شامل ستون‌های زیر است:

Title: عنوان کتاب

Author: نویسنده

First Publish Year: سال اولین انتشار

Publisher: ناشر

مثال استفاده
# اجرای اسکریپت
python main.py
خروجی:
یک فایل CSV شامل ۵۰ کتاب بعد از سال ۲۰۰۰.

نکات مهم
اگر کمتر از ۵۰ کتاب بعد از سال ۲۰۰۰ پیدا شد، ممکن است به دلیل محدودیت دیتابیس OpenLibrary باشد.

فایل CSV به طور پیش‌فرض کنار فایل main.py ساخته می‌شود.

فایل CSV می‌تواند توسط Excel، Google Sheets یا Python خوانده شود.

