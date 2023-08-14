#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

# دریافت محتوای وب‌سایت حاوی لیست کلمات فارسی
url = "https://vajehyab.com/"
response = requests.get(url)
farsi_words = response.text.split()

# نوشتن لیست کلمات در یک فایل
with open("farsi_words.txt", "w", encoding="utf-8") as file:
    for word in farsi_words:
        file.write(word + "\n")

print("فایل با موفقیت ایجاد شد.")


# In[ ]:




