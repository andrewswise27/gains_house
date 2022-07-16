import pdb
from models.session import Session
from models.gym import Gym
from models.member import Member

import repositories.gym_repository as gym_repo
import repositories.member_repository as member_repo
import repositories.session_repository as session_repo

session1 = Session('Body Pump', '12:00', '22-09-22', 60, 10, "BODYPUMP is a fast-paced, barbell-based workout that's specifically designed to help you get lean, toned and fit.", 'Expert')
session2 = Session('Hot Yoga','12:30', '22-09-22', 80, 12, 'Hot yoga is a vigorous form of yoga performed in a very warm and humid studio.', 'Intermediate')
session_repo.save(session1)
session_repo.save(session2)

# sessions = session_repo.select_all()
# for session in sessions:
#     print(session.__dict__)

gym1 = Gym('The Gains House', 'Edinburgh')
gym_repo.save(gym1)