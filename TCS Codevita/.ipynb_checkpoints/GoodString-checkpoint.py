import bisect

def get_total_distance(good_string, name):
    prev_good_letter = good_string[0]
    
    good_string_chars = sorted([ord(ch) for ch in good_string])
    good_string_set = set(good_string)
    total_distance = 0
    
    for c in name:
        if c == ' ' or c in good_string_set:
            continue 
        else:
            ord_c = ord(c)
            pos = bisect.bisect_left(good_string_chars, ord_c)
            candidates = []
            min_distance = None

            if pos > 0:
                left_ord = good_string_chars[pos - 1]
                distance = abs(ord_c - left_ord)
                candidates.append((distance, left_ord))

            if pos < len(good_string_chars):
                right_ord = good_string_chars[pos]
                distance = abs(ord_c - right_ord)
                candidates.append((distance, right_ord))

            min_distance = min(candidates, key=lambda x: x[0])[0]
            candidates_with_min_distance = [cand for cand in candidates if cand[0] == min_distance]

            if len(candidates_with_min_distance) == 1:
                selected_letter_ord = candidates_with_min_distance[0][1]
                distance = abs(ord_c - selected_letter_ord)
            else:
                min_prev_distance = None
                selected_letter_ord = None
                for _, cand_ord in candidates_with_min_distance:
                    prev_distance = abs(cand_ord - ord(prev_good_letter))
                    if min_prev_distance is None or prev_distance < min_prev_distance:
                        min_prev_distance = prev_distance
                        selected_letter_ord = cand_ord
                    elif prev_distance == min_prev_distance:
                        if cand_ord < selected_letter_ord:
                            selected_letter_ord = cand_ord

                distance = abs(ord(prev_good_letter) - selected_letter_ord)

            prev_good_letter = chr(selected_letter_ord)
            total_distance += distance

    return total_distance

good_string = input().strip()
name = input().strip()

result = get_total_distance(good_string, name)

print(result)