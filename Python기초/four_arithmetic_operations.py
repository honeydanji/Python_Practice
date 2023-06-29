#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 사칙연산
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0:
         return "0으로 나눌 수 없습니다."  
    else:
         return a / b
     

