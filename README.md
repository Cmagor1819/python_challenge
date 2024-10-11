# python_challenge
I got/Referenced the followwing lines of code from Xpert Learning Assistant/GitHub

changes = []
    for i in range(1, len(total_net)):
        change = total_net[i] - total_net[i - 1]
        changes.append(change)
        
for x in election_dict:
    output_line_5 = (f"{x}: {format(float(election_dict[x] / total_votes) , ' .3%')} ({election_dict[x]})")
    print(output_line_5)

for candidate in candidates:
        vote_count.append(total_candidates.count(candidate))

winning_candidate = max(election_dict, key=election_dict.get)

