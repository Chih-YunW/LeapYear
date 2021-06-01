import leapYear

def test_not_divisible_by_4():
	value = (1999)
	assert leapYear.leapYear(value) == "It is not a leap year"
def test__divisible_by_4_and_100():
        value = (2000)
        assert leapYear.leapYear(value) == "It is a leap year"

