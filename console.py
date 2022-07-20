import pdb

from psycopg2 import Timestamp
from models.session import Session
from models.booked_session import BookedSession
from models.member import Member
from datetime import datetime

import repositories.booked_session_repository as booked_session_repo
import repositories.member_repository as member_repo
import repositories.session_repository as session_repo

session_repo.delete_all()
member_repo.delete_all()

session1 = Session('Body Pump', '2022-09-22 12:00:00', 60, 10, "BODYPUMP is a fast-paced, barbell-based workout that's specifically designed to help you get lean, toned and fit.", 'Expert')
session2 = Session('Hot Yoga','2022-09-22 12:30:00', 80, 12, 'Hot yoga is a vigorous form of yoga performed in a very warm and humid studio.', 'Intermediate')
session3 = Session('Yoga', '2022-09-22 13:00:00', 80, 10, 'Yoga is a mind and body practice. Various styles of yoga combine physical postures, breathing techniques, and meditation or relaxation.', 'Beginner')
session4 = Session('Zumba', '2022-09-22 13:30:00', 45, 20, 'Zumba is a form of fitness class in which you burn off calories by dancing to different kinds of lively tunes.', 'Beginner')
session5 = Session('Crossfit', '2022-09-22 14:00:00', 120, 8, 'A form of high intensity interval training, CrossFit is a strength and conditioning workout that is made up of functional movement performed at a high intensity level.', 'Expert')
session6 = Session('HIIT', '2022-09-22 14:30:00', 40, 14, 'This type of training involves repeated bouts of high intensity effort followed by varied recovery times.', 'Beginner')
session7 = Session('Hot Yoga', '2022-07-26 12:00:00', 75, 10, 'Expert', 'Hot yoga is a vigorous form of yoga performed in a very warm and humid studio.')
session8 = Session('Crossfit', '2022-07-28 13:30:00', 75, 8, 'Intermediate', 'A form of high intensity interval training, CrossFit is a strength and conditioning workout that is made up of functional movement performed at a high intensity level.')
session9 = Session('Vinyasa Yoga', '2022-07-28 12:00:00', 65, 10, 'Intermediate', 'A Vinyasa yoga practice connects individual poses or “asanas” with deep breaths or “pranayama” in a series of flowing sequences of movement. Designed to progressively open the body, each sequence in a Vinyasa yoga class builds upon the previous, evolving into deeper, more advanced postures as the practice unfolds.')
session10 = Session('Vinyasa Yoga', '2022-07-28 17:00:00', 65, 10, 'Intermediate', 'A Vinyasa yoga practice connects individual poses or “asanas” with deep breaths or “pranayama” in a series of flowing sequences of movement. Designed to progressively open the body, each sequence in a Vinyasa yoga class builds upon the previous, evolving into deeper, more advanced postures as the practice unfolds.')
session11 = Session('Vinyasa Yoga', '2022-08-04 12:00:00', 65, 10, 'Intermediate', 'A Vinyasa yoga practice connects individual poses or “asanas” with deep breaths or “pranayama” in a series of flowing sequences of movement. Designed to progressively open the body, each sequence in a Vinyasa yoga class builds upon the previous, evolving into deeper, more advanced postures as the practice unfolds.')
session12 = Session('Vinyasa Yoga',	'2022-08-04 17:00:00', 65, 10, 'Intermediate', 'A Vinyasa yoga practice connects individual poses or “asanas” with deep breaths or “pranayama” in a series of flowing sequences of movement. Designed to progressively open the body, each sequence in a Vinyasa yoga class builds upon the previous, evolving into deeper, more advanced postures as the practice unfolds.')
session13 = Session('Body Pump', '2022-08-03 09:00:00', 45, 10, 'Beginner', "BODYPUMP is a fast-paced, barbell-based workout that's specifically designed to help you get lean, toned and fit.")
session14 = Session('Body Pump', '2022-08-03 15:00:00', 45, 10, 'Beginner', "BODYPUMP is a fast-paced, barbell-based workout that's specifically designed to help you get lean, toned and fit.")
session15 = Session('Zumba', '2022-08-06 18:00:00', 60, 8, 'Intermediate', "Zumba is a form of fitness class in which you burn off calories by dancing to different kinds of lively tunes.")
session16 = Session('Zumba', '2022-08-06 21:00:00', 60, 8, 'Intermediate', "Zumba is a form of fitness class in which you burn off calories by dancing to different kinds of lively tunes.")
session17 = Session('Vinyasa Yoga', '2023-01-01 17:00:00', 100, 1, 'Beginner', 'A Vinyasa yoga practice connects individual poses or “asanas” with deep breaths or “pranayama” in a series of flowing sequences of movement. Designed to progressively open the body, each sequence in a Vinyasa yoga class builds upon the previous, evolving into deeper, more advanced postures as the practice unfolds.')
session_repo.save(session1)
session_repo.save(session2)
session_repo.save(session3)
session_repo.save(session4)
session_repo.save(session5)
session_repo.save(session6)
session_repo.save(session7)
session_repo.save(session8)
session_repo.save(session9)
session_repo.save(session10)
session_repo.save(session11)
session_repo.save(session11)
session_repo.save(session12)
session_repo.save(session13)
session_repo.save(session14)
session_repo.save(session15)
session_repo.save(session16)
session_repo.save(session17)

member1 = Member('Chris', 25, 'British', '07546727384', 'holt_hogan@gains.co.uk', 'Gold')
member2 = Member('Nathan', 30, 'British', '07625738192', 'kawasaki_ninja@gains.co.uk', 'Bronze')
member3 = Member('Stuart', 21, 'British', '07829384761', 'young_guns@gains.co.uk', 'Bronze')
member4 = Member('Jack', 25, 'British', '07716253891', 'pingpong_champ@gains.co.uk', 'Gold')
member5 = Member('John Bones', 34, 'American', '07645372617', 'bones_jones@gains.co.uk', 'Gold')
member6 = Member('Goldberg', 50, 'American', '07523645172',	'the_spear@gainsco.uk', 'Gold')
member7 = Member('Big Show', 52, 'American', '07635471625', 'big_lad@gains.co.uk', 'Bronze')
member8 = Member('Mark Henry', 48, 'American', '07462517261', 'strongest_man@gains.co.uk', 'Gold')
member9 = Member('Daz', 24, 'British', '07354615262', 'roids@gains.co.uk', 'Gold')


member_repo.save(member1)
member_repo.save(member2)
member_repo.save(member3)
member_repo.save(member4)
member_repo.save(member5)
member_repo.save(member6)
member_repo.save(member7)
member_repo.save(member8)
member_repo.save(member9)

