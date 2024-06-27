Name_Waterproof = {'T-100':0.35,'T-200':0.35,'T-200H':0.35,'NPU-12E':0.35,'SPU-1000_1mm':1.2,'SPU-1000_2mm':2.4,'SPU-1000_3mm':3.6}



print('------ โปรแกรมคำนวณความหนาฟิล์ม By CB ------')
try:
    Name_Waterproof = input('ชื่อสินค้ากันซึม? [T-100 / T-200 / T-200H / NPU-12E / SPU-1000]: ')
    Density = float(input('Density?: '))
    Consumtion = float(input('ปริมาณการใช้งาน 1 ตารางเมตร 1 รอบ: '))
    Layer = int(input('ต้องการทากันซึมกี่รอบ: '))
    SolidContent = int(input('%Solidเท่าไร?: '))
    
    Goal_Tickness = float(input('ถ้าต้องการฟิล์มแห้งหนา?(Micron): '))   
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!')
    Name_Waterproof = input('ชื่อสินค้ากันซึม? [T-100 / T-200 / T-200H / NPU-12E / SPU-1000]: ')
    Density = float(input('Density?: '))
    Consumtion = float(input('ปริมาณการใช้งาน 1 ตารางเมตร 1 รอบ: '))
    Layer = int(input('ต้องการทากันซึมกี่รอบ: '))
    SolidContent = int(input('%Solidเท่าไร?: '))
    
    Goal_Tickness = float(input('ถ้าต้องการฟิล์มแห้งหนา?(Micron): '))  

   
    
print('------Calculate------')

Wet_Film = 1000 * Consumtion /  Density
Dry_film = Wet_Film * SolidContent / 100
Numer_layer_for_thickness = Goal_Tickness / Dry_film




print(f'สินค้ากันซึม: {Name_Waterproof} ')

print('------คำนวณการใช้งานโดยทั่วไป------')
print('ความหนาฟิล์มเปียก {} Micron'.format(Wet_Film))
print('ความหนาฟิล์มแห้ง {} Micron'.format(Dry_film))

print('------คำนวณจำนวนรอบที่ต้องทาให้ได้ความหนาที่ต้องการ------')
print('ความหนาที่ต้องการต้องทา {} รอบ'.format(Numer_layer_for_thickness))

