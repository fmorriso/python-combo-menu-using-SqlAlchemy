import sys
import sqlalchemy as sa


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_SqlAlchemy_version() -> str:
    return sa.__version__


if __name__ == '__main__':
    print(f'Combo Menu via SqlAlchemy using python version {get_python_version()}')
    print(f'and SQLAlchemy version {get_SqlAlchemy_version()}')