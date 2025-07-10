import random,json
from faker import Faker
fake = Faker()
def fake_contact(gender):
    def base_fields():
        return {
            "company": fake.company(),
            "job_title": fake.job(),
            "department": fake.bs().split()[0],  # just a fake department word
            "phone_home": fake.phone_number(),
            "phone_mobile": fake.phone_number(),
            "phone_work": fake.phone_number(),
            "phone_fax": fake.phone_number(),
            "address_home_street": fake.street_address(),
            "address_home_city": fake.city(),
            "address_home_country": fake.country(),
            "birthday": str(fake.date_of_birth(minimum_age=18, maximum_age=65)),
            "website": fake.url(),
            "notes": fake.sentence(),
            "relationship": random.choice(['friend', 'coworker', 'family', 'acquaintance']),
            "custom_fields": json.dumps({"favorite_color": fake.color_name()})
        }

    if gender == 'male':
        first_name = fake.first_name_male()
        middle_name = fake.first_name_male()
        last_name = fake.last_name_male()
        nickname = fake.user_name()
        title = fake.prefix_male()
    elif gender == 'female':
        first_name = fake.first_name_female()
        middle_name = fake.first_name_female()
        last_name = fake.last_name_female()
        nickname = fake.user_name()
        title = fake.prefix_female()
    else:
        first_name = fake.first_name_nonbinary()
        middle_name = fake.first_name_nonbinary()
        last_name = fake.last_name_nonbinary()
        nickname = fake.user_name()
        title = fake.prefix_nonbinary()

    base = base_fields()

    return (
        first_name,
        middle_name,
        last_name,
        nickname,
        title,
        base["company"],
        base["job_title"],
        base["department"],
        base["phone_home"],
        base["phone_mobile"],
        base["phone_work"],
        base["phone_fax"],
        base["address_home_street"],
        base["address_home_city"],
        base["address_home_country"],
        base["birthday"],
        base["website"],
        base["notes"],
        base["relationship"],
        base["custom_fields"]
    )

def list_of_many_fakes(amount,gender):
    _list = []
    while amount != 0:
        _list.append(fake_contact(gender))
        amount -= 1
    return _list