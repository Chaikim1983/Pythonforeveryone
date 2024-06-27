Name_Waterproof = {'T-100':0.35,'T-200':0.35,'T-200H':0.35,'NPU-12E':0.35,'SPU-1000_1mm':1.2,'SPU-1000_2mm':2.4,'SPU-1000_3mm':3.6}
volume_Waterproof = {'T-100-1set':20,'T-200-1set':20,'T-200H-1set':20,'NPU-12E-1set':11,'SPU-1000_1mm-1set':42.5,'SPU-1000_2mm-1set':42.5,'SPU-1000_3mm-1set':42.5}


print('------ โปรแกรมคำนวณการใช้กันซึม By CB ------')
try:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!')
    Area = float(input('พื้นที่ที่ต้องทำระบบกันซึมทั้งหมดกี่ตารางเมตร: '))
    Name_Waterproof = input('ชื่อสินค้ากันซึม? [T-100 / T-200 / T-200H / NPU-12E / SPU-1000]: ')
    Consumtion = float(input('ปริมาณการใช้งาน 1 ตารางเมตร 1 รอบ: '))
    Product_Weight_1set = float(input('น้ำหนักสินค้า 1 ชุด: '))
    Layer = int(input('ต้องการทากันซึมกี่รอบ: '))   
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!')
    Area = float(input('พื้นที่ที่ต้องทำระบบกันซึมทั้งหมดกี่ตารางเมตร: '))
    Name_Waterproof = input('ชื่อสินค้ากันซึม? [T-100 / T-200 / T-200H / NPU-12E / SPU-1000]: ')
    Consumtion = float(input('ปริมาณการใช้งาน 1 ตารางเมตร 1 รอบ: '))
    Product_Weight_1set = float(input('น้ำหนักสินค้า 1 ชุด: '))
    Layer = int(input('ต้องการทากันซึมกี่รอบ: ')) 

    #volume_Waterproof = input('สินค้ากันซึม-1-ชุด? [T-100-1set / T-200-1set / T-200H-1set / NPU-12E-1set / SSPU-1000_1mm-1set / SPU-1000_2mm-1set / SPU-1000_3mm-1set]: ')
    
print('------Calculate------')

total_Waterproof = Area * Layer * Consumtion 
Pail_Waterproof = total_Waterproof / Product_Weight_1set

# print(total_row,remain_tiles)

# buy_more = row - remain_tiles

print(f'พื้นที่ที่ต้องทำระบบกันซึมทั้งหมด: {Area} ตารางเมตร')
print(f'สินค้ากันซึม: {Name_Waterproof} ')
print('------คำนวณ------')
print('ต้องใช้กันซึมทั้งหมด {} กิโลกรัม'.format(total_Waterproof))
print('ต้องใช้กันซึมทั้งหมด {} ชุด'.format(Pail_Waterproof))
#print('ลูกค้าต้องซื้อกระเบื้องเพิ่ม {} แผ่น'.format(buy_more))
#print('ยอดรวมทั้งหมดที่ต้องซื้อกระเบื้องเพิ่ม: {} บาท'.format(buy_more * tilecolor[color]))
#ลูกค้าต้องซื้อกระเบื้องเพิ่มกี่แผ่น
#เปลี่ยน tiles = 10 -> 1456 ; row = 3 -> 53
