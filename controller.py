''' ./controllyer.py'''
from modelStudent.meeting import Meeting



def main():
    '''the main function to control this app'''
    curr_meeting = Meeting(
        start_time="0:00 AM", end_time="12:00 AM", id_meeting="123", name_meeting="hello")
    i = int(input())
    while i == 0:
        print(Meeting.print_info_meeting(curr_meeting))
        i = int(input())
