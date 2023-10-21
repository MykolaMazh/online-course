from __future__ import annotations


class OnlineCourse:
    @staticmethod
    def days_to_weeks(days: int) -> int:
        return (days // 7) + 1 if days % 7 != 0 else days // 7

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )

    def __init__(
            self,
            name: str,
            description: str,
            weeks: int
    ) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
