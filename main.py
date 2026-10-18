import turtle

# ==========================================
# 1. إعداد الشاشة والسلحفاة / Screen & Turtle Setup
# ==========================================
screen = turtle.Screen()
screen.bgcolor("black")  # خلفية سوداء لإبراز الألوان الساطعة / Black background to highlight colors

t = turtle.Turtle()
t.speed(0)  # ضبط السرعة على أقصى درجة / Set speed to maximum for fast rendering

# ==========================================
# 2. الألوان والحلقة التكرارية / Colors & Main Loop
# ==========================================
# قائمة الألوان المتدرجة / Array of vibrant colors
colors = ["red", "yellow", "blue", "green", "purple", "orange", "cyan"]

# رسم الشكل الهندسي عبر 360 تكرار / Draw pattern using 360 iterations
for i in range(360):
    t.color(colors[i % len(colors)])  # التبديل الدوري بين الألوان / Cycle through color list
    t.width(i / 100 + 1)              # زيادة سمك القلم تدريجياً / Gradually increase pen width
    t.forward(i)                      # التحرك للأمام بمسافة تزيد مع كل خطوة / Move forward
    t.left(59)                        # الدوران بزاوية 59 درجة لتشكيل النمط / Turn left by 59 degrees

# إبقاء النافذة مفتوحة حتى إغلاقها / Keep window open
turtle.done()
