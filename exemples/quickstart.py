import time
import pratik

pratik.clear()
print("*It was a long time ago somewhere in the files of the", pratik.get_root(), "folder*")
print("Young child: Venerable ancestor, how old are you?")
age = pratik.enter("You: Venerable ancestor... Venerable ancestor... Oh, come on! I only have ")
print("Young child:", pratik.humanize_number(age ** 2) if age ** 2 > 999 else age ** 2, "years! That's huge!")
print("You: You cheeky little one!! Feel the time I've spent and adore me!")
divide = pratik.gcd(age, 2 * 3 * 5 * 7)
for x in range(10):
    pratik.progress_bar(x, (age * 31536000), width=20)
    time.sleep(1)
print(
    "\rYou: Okay. I'm bored. Go away and I won't see you again! "
    "For", ((str(divide) + 'years') if divide > 1 else 'a year') + "!!"
)
