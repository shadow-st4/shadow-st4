from tkinter import *

root = Tk()
root.title('contact-maker')
root.resizable(width=False, height=False)

Font = ('arial', 18, '')

#lbl-for-space >>
Label(root, text='\n').pack(expand=True, fill=BOTH)

#body >>>
Label(root, text='\tenter phone number wirhout zero!\t', font=Font).pack()
Label(root, text='\n').pack(expand=True, fill=BOTH)

#----------option's
def create_member():
    make = ''
    while True:
        number = From.get()
        number = int(number)
        x = To.get()
        x = int(x)
        name = Name.get()
        name = str(name)
        contact = To.get()
        contact = str(contact)
        contact += '.vcf'
        if number < x:
            break
        
    while number < x:
        number += 1
        BEGIN = 'BEGIN:VCARD\n'
        make += BEGIN
        VER = 'VERSION:2.1\n'
        make += VER
        NAME = f'N:;{name};;;\n'
        make += NAME
        FIRSTNAME = f'FN:{name}\n'
        make += FIRSTNAME
        TEL = f'TEL;CELL:+98{number}\n'
        make += TEL
        END = 'END:VCARD\n'
        make += END
        
    with open(contact,'a') as f:
        f.write(make)


#----------phone-number
Label(root, text='name your contact:', font=Font).pack()
Name = Entry(root, font=Font)
Name.pack()

Label(root, text='from:', font=Font).pack()
From = Entry(root, font=Font)
From.pack()

Label(root, text='to:', font=Font).pack()
To = Entry(root, font=Font)
To.pack()

Label(root, text='\n').pack(expand=True, fill=BOTH)

Button(root, text='creat', font=Font, command=create_member).pack()

Label(root, text='\n').pack(expand=True, fill=BOTH)

root.mainloop()
