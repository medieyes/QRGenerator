import qrcode
from tkinter import *;
import tkinter.messagebox as msgbox

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=4,
    border=4,
)



root = Tk()
root.title('약리미 QR코드')
root.geometry("620x600")

# 고객명 줄
lb_cusname = Label(root, text="고객명", width=10, height=2, font=20)
txt_cusname = Entry(root,width=55, font=20)

lb_cusname.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=15)
txt_cusname.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=15)

# 약 이름
lb_mediname = Label(root, text="약 이름", width=10, height=2, font=20)
txt_mediname = Entry(root,width=55, font=20)

lb_mediname.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=15)
txt_mediname.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=15)

# 복용법
lb_howeat = Label(root, text="복용법", width=10, height=2, font=20)
txt_howeat = Entry(root,width=55, font=20)

lb_howeat.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=15)
txt_howeat.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=15)

# 효능, 효과
lb_effect = Label(root, text="효능, 효과", width=10, height=2, font=20)
txt_effect = Text(root,width=30, height=10)

lb_effect.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=15)
txt_effect.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=15)

# 주의사항
lb_caution = Label(root, text="주의사항", width=10, height=2, font=20)
txt_caution = Text(root,width=30, height=10)

lb_caution.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=15)
txt_caution.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=15)


def btncmd():
    info = "medieye:/"+txt_mediname.get()+"/"+txt_howeat.get()+"/"+txt_effect.get("1.0", END)+"/"+txt_caution.get("1.0", END)
    print(info)
    qr.add_data(info)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('./QRimg/'+txt_cusname.get()+".png")
    msgbox.showinfo("알림", "정상적으로 완성되었습니다.")
    
btn_qr = Button(root, text="QRcode 생성", command=btncmd)
btn_qr.grid(row=5, column=1, sticky=N+E+W+S, padx=3, pady=15)

root.mainloop()



# 타리레놀 500밀리그램

# 1회 1~2정 1일 3~4회 (4시간마다)

# 감기로 인한 발열 및 통증, 두통, 신경통, 근육통, 월경통, 염좌통(삔통증), 치통, 관절통, 류마티양 통증

# 이 약에 과민증 환자, 소화성 궤양 환자, 심한 혈액 이상 환자, 심한 간장애 환자, 심한 신장 장애 환자는 이약을 복용하지 말것
# 간장애 또는 그 병력이 있는 환자는 복용하기 전에 의사, 약사와 상의할 것		