import pdb
from models.session import Session
from models.gym import Gym
from models.member import Member

import repositories.gym_repository as gym_repo
import repositories.member_repository as member_repo
import repositories.session_repository as session_repo

session_repo.delete_all()
gym_repo.delete_all()
member_repo.delete_all()

session1 = Session('Body Pump', '2022-09-22 12:00:00', 60, 10, "BODYPUMP is a fast-paced, barbell-based workout that's specifically designed to help you get lean, toned and fit.", 'Expert')
session2 = Session('Hot Yoga','2022-09-22 12:30:00', 80, 12, 'Hot yoga is a vigorous form of yoga performed in a very warm and humid studio.', 'Intermediate')
session3 = Session('Yoga', '2022-09-22 13:00:00', 80, 10, 'Yoga is a mind and body practice. Various styles of yoga combine physical postures, breathing techniques, and meditation or relaxation.', 'Beginner')
session4 = Session('Zumba', '2022-09-22 13:30:00', 45, 20, 'Zumba is a form of fitness class in which you burn off calories by dancing to different kinds of lively tunes.', 'Beginner')
session5 = Session('Crossfit', '2022-09-22 14:00:00', 120, 8, 'A form of high intensity interval training, CrossFit is a strength and conditioning workout that is made up of functional movement performed at a high intensity level.', 'Expert')
session6 = Session('HIIT', '2022-09-22 14:30:00', 40, 14, 'This type of training involves repeated bouts of high intensity effort followed by varied recovery times.', 'Beginner')
session_repo.save(session1)
session_repo.save(session2)
session_repo.save(session3)
session_repo.save(session4)
session_repo.save(session5)
session_repo.save(session6)

member1 = Member('Chris', 25, 'British', '07546727384', 'holt_hogan@gains.co.uk')
member2 = Member('Nathan', 30, 'British', '07625738192', 'kawasaki_ninja@gains.co.uk')
member3 = Member('Stuart', 21, 'British', '07829384761', 'young_guns@gains.co.uk')
member4 = Member('Jack', 25, 'British', '07716253891', 'pingpong_champ@gains.co.uk')

member_repo.save(member1)
member_repo.save(member2)
member_repo.save(member3)
member_repo.save(member4)

# sessions = session_repo.select_all()
# for session in sessions:
#     print(session.__dict__)

gym1 = Gym('The Gains House', 'Edinburgh')
gym_repo.save(gym1)