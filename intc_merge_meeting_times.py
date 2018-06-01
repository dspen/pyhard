def merge_ranges(meetings):
    sorted_meetings = sorted(meetings);

    merged_meetings = [sorted_meetings[0]];

    for start, end in sorted_meetings[1:]:
        last_start, last_end = merged_meetings[-1];

        if (start <= last_end):
            merged_meetings[-1] = (last_start, max(last_end, end));

        else:
            merged_meetings.append((start,end));

    return merged_meetings;


#
# def merge_ranges(meetings):
#     # Sort by start time
#     sorted_meetings = sorted(meetings)
#
#     # Initialize merged_meetings with the earliest meeting
#     merged_meetings = [sorted_meetings[0]]
#
#     for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
#         last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
#
#         # If the current meeting overlaps with the last merged meeting, use the
#         # later end time of the two
#         if (current_meeting_start <= last_merged_meeting_end):
#             merged_meetings[-1] = (last_merged_meeting_start,
#                                    max(last_merged_meeting_end,
#                                        current_meeting_end))
#         else:
#             # Add the current meeting since it doesn't overlap
#             merged_meetings.append((current_meeting_start, current_meeting_end))
#
#     return merged_meetings

print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
