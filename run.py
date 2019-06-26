from cookiespool.scheduler import Scheduler
from cookiespool.importer import scan

def main():
    scan()
    s = Scheduler()
    s.run()

if __name__ == '__main__':
    main()