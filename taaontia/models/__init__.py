from sqlalchemy_utils import force_auto_coercion

force_auto_coercion()

from .user import User
from .statistics import Statistics
