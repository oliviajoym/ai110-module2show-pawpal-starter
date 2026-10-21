from datetime import date

from pawpal_system import (
    Frequency,
    Owner,
    Pet,
    Scheduler,
    Task,
    TimeOfDay,
)


def build_sample_data() -> Owner:
    owner = Owner(owner_id="O1", name="Jamie")

    dog = Pet(pet_id="P1", name="Rex", species="Dog", owner=owner)
    cat = Pet(pet_id="P2", name="Whiskers", species="Cat", owner=owner)
    owner.add_pet(dog)
    owner.add_pet(cat)

    morning_walk = Task(
        task_id="T1",
        description="Morning walk",
        time_constraint=TimeOfDay.MORNING,
        repeated=True,
        frequency=Frequency.DAILY,
        owner_presence_required=True,
        pet=dog,
        next_due_date=date.today(),
    )

    vet_visit = Task(
        task_id="T2",
        description="Vet checkup",
        time_constraint=TimeOfDay.AFTERNOON,
        repeated=False,
        frequency=None,
        owner_presence_required=True,
        pet=dog,
        next_due_date=date.today(),
    )

    feed_cat = Task(
        task_id="T3",
        description="Evening feeding",
        time_constraint=TimeOfDay.EVENING,
        repeated=True,
        frequency=Frequency.DAILY,
        owner_presence_required=False,
        pet=cat,
        next_due_date=date.today(),
    )

    scheduler = Scheduler(owner=owner)
    scheduler.schedule_task(morning_walk)
    scheduler.schedule_task(vet_visit)
    scheduler.schedule_task(feed_cat)

    return owner


def print_todays_schedule(scheduler: Scheduler) -> None:
    print("=== Today's Schedule ===")
    for time_slot in (TimeOfDay.MORNING, TimeOfDay.AFTERNOON, TimeOfDay.EVENING):
        tasks = scheduler.get_tasks_by_time(time_slot)
        if not tasks:
            continue
        print(f"\n{time_slot.value.capitalize()}:")
        for task in tasks:
            owner_note = " (owner must be present)" if task.owner_presence_required else ""
            print(f"  - [{task.pet.name}] {task.description}{owner_note}")


def main() -> None:
    owner = build_sample_data()
    scheduler = Scheduler(owner=owner)
    print_todays_schedule(scheduler)


if __name__ == "__main__":
    main()