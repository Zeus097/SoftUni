import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import QuerySet, F
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character
from decimal import Decimal
from main_app.choices import CharacterNameChoices


def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(
        name=name,
        species=species,
    )
    pet.save()

    return f"{pet.name} is a very cute {pet.species}!"


# # Test code
#
# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )
    artifact.save()

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


# # Test code
#
# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)


def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')
    return "\n".join(f"{l.name} has a population of {l.population}!" for l in locations)


def new_capital():
    first_location = Location.objects.first()
    first_location.is_capital = True
    first_location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


# # Test code
#
# print(show_all_locations())
# print(new_capital())
# print(get_capitals())


def apply_discount() -> None:
    cars = Car.objects.all()
    for car in cars:
        percentage_off = Decimal(str(sum(int(digit) for digit in str(car.year)) / 100))
        discount = car.price * percentage_off
        car.price_with_discount = car.price - discount
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


# # Test code
#
# apply_discount()
# print(get_recent_cars())


def show_unfinished_tasks():
    # unfinished_tasks = Task.objects.filter(is_finished=False).values('title', 'due_date')
    # tasks_ls = []
    # for task in unfinished_tasks:
    #     tasks_ls.append(f"Task - {task['title']} needs to be done until {task['due_date']}!")
    # return "\n".join(tasks_ls)

    task = Task.objects.filter(is_finished=False)
    return "\n".join(f"Task - {t.title} needs to be done until {t.due_date}!" for t in task)


def complete_odd_tasks():
    tasks = Task.objects.all()
    for task in tasks:
        print(task.id)
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    encoded_text = ''.join(chr(ord(word) - 3) for word in text)

    for task in Task.objects.filter(title=task_title):
        task.description = encoded_text
        task.save()


# # Test code
#
# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title='Simple Task').description)


def get_deluxe_rooms():
    rooms = HotelRoom.objects.all()
    room_ls = []
    for room in rooms:
        if room.id % 2 == 0 and room.room_type == 'Deluxe':
            room_ls.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")
    return "\n".join(room_ls)


def increase_room_capacity():
    rooms = HotelRoom.objects.filter(is_reserved=True).order_by('id')
    previous_room: HotelRoom = None

    for room in rooms:
        if previous_room:
            room.capacity += previous_room.capacity
        else:
            room.capacity += room.id

        previous_room = room
        room.save()


def reserve_first_room():
    reserved_room = HotelRoom.objects.first()
    reserved_room.is_reserved = True
    reserved_room.save()


def delete_last_room():
    room = HotelRoom.objects.last()
    r = room.room_number
    if not room.is_reserved:
        room.delete()


# # Test code
#
# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=401).is_reserved)


def update_characters():

    Character.objects.filter(class_name=CharacterNameChoices.MAGE).update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7,
    )

    Character.objects.filter(class_name=CharacterNameChoices.WARRIOR).update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4,
    )

    Character.objects.filter(class_name__in=[CharacterNameChoices.ASSASSIN, CharacterNameChoices.SCOUT]).update(
        inventory='The inventory is empty',
    )


def fuse_characters(first_character: Character, second_character: Character):
    fusion_inventory = None

    if first_character.class_name in [CharacterNameChoices.MAGE, CharacterNameChoices.SCOUT]:
        fusion_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    elif first_character.class_name in [CharacterNameChoices.WARRIOR, CharacterNameChoices.ASSASSIN]:
        fusion_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=first_character.name + ' ' + second_character.name,
        class_name=CharacterNameChoices.FUSION,
        level=(first_character.level + second_character.level) // 2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity=(first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=(first_character.hit_points + second_character.hit_points),
        inventory=fusion_inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()


# # Test code
#
# character1 = Character.objects.create(
#     name='Gandalf',
#     class_name='Mage',
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory='Staff of Magic, Spellbook',
# )
#
# character2 = Character.objects.create(
#     name='Hector',
#     class_name='Warrior',
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory='Sword of Troy, Shield of Protection',
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)


# Output
#
# Gandalf Hector
# Fusion
# 11
# 52
# Bow of the Elven Lords, Amulet of Eternal Wisdom








