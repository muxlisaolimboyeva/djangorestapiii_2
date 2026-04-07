# 1. API (Application Programming Interface) nima?
# API — bu ikki dastur bir-biri bilan muloqot qilishi uchun yaratilgan interfeys.

# Oddiy qilib aytganda:
# API — bu bir dasturdan boshqa dasturga ma'lumot olish yoki yuborish usuli.


# Real hayotdagi misol
# Restoranni tasavvur qiling:
# Mijoz → buyurtma beradi
# Ofitsiant → buyurtmani oshxonaga olib boradi
# Oshxona → ovqat tayyorlaydi

# Bu yerda:
# Rol	Dasturdagi analog
# Mijoz	- Frontend
# Ofitsiant	- API
# Oshxona - Backend / Database


# API qanday ishlaydi
# Masalan siz mahsulotlarni olishni xohlaysiz.
# Frontend serverga so‘rov yuboradi:
# GET /products
# Server javob beradi:
#
# [
#  {
#    "id":1,
#    "title":"Iphone 15",
#    "price":1200
#  },
#  {
#    "id":2,
#    "title":"Samsung S24",
#    "price":1000
#  }
# ]
#
# Bu JSON formatdagi javob.


# 2. REST API nima?
# REST API — bu API yaratish uchun ishlatiladigan standart arxitektura usuli.
# REST ning to‘liq nomi:
# Representational State Transfer


# REST API HTTP metodlari
# REST API HTTP metodlari orqali ishlaydi.
# Method Vazifasi


# GET	Ma'lumot olish
# POST	Yangi ma'lumot qo‘shish
# PUT	To‘liq yangilash
# PATCH	Qisman yangilash
# DELETE	O‘chirish


