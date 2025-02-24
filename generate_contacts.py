import random
import faker

# 初始化Faker库
fake = faker.Faker('zh_CN')

# 随机选择称呼
titles = ['先生', '女士', '老师', '同学', '朋友', '老板', '家人']

# 随机选择关系
relationships = ['家人', '同事', '同学', '朋友']


# 生成一个符合中国手机规则的手机号
def generate_chinese_phone_number():
    # 中国手机号通常以13、14、15、16、17、18、19开头，后面8位随机生成
    prefix = random.choice(['13', '14', '15', '16', '17', '18', '19'])
    number = ''.join(random.choices('0123456789', k=8))
    return prefix + number


# 生成一个vCard格式的联系人字符串
def generate_vcard(name, phone, title, relationship):
    vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name} {title}
TEL:{phone}
X-RELATIONSHIP:{relationship}
END:VCARD
"""
    return vcard


# 生成一个文本格式的联系人字符串
def generate_txt(name, phone, title, relationship):
    txt = f"姓名: {name} {title}\n手机号: {phone}\n关系: {relationship}\n\n"
    return txt


# 随机生成30个联系人
def generate_contacts(num_contacts=30):
    contacts_vcf = []
    contacts_txt = []
    for _ in range(num_contacts):
        name = fake.name()  # 随机生成中文名字
        phone = generate_chinese_phone_number()  # 使用自定义方法生成中国手机号
        title = random.choice(titles)  # 随机选一个称呼
        relationship = random.choice(relationships)  # 随机选择一个关系

        # 生成vCard格式和文本格式的联系人
        contacts_vcf.append(generate_vcard(name, phone, title, relationship))
        contacts_txt.append(generate_txt(name, phone, title, relationship))

    return contacts_vcf, contacts_txt


# 将联系人保存到.vcf文件
def save_contacts_to_vcf(contacts_vcf, filename='contacts.vcf'):
    with open(filename, 'w', encoding='utf-8') as f:
        for contact in contacts_vcf:
            f.write(contact)
    print(f"Contacts saved to {filename}")


# 将联系人保存到.txt文件
def save_contacts_to_txt(contacts_txt, filename='contacts.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for contact in contacts_txt:
            f.write(contact)
    print(f"Contacts saved to {filename}")


# 生成并保存联系人
contacts_vcf, contacts_txt = generate_contacts()
save_contacts_to_vcf(contacts_vcf)
save_contacts_to_txt(contacts_txt)
