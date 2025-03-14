from collections import deque
'''
 یک صف دوطرفه (Double ended queue یا dequeue)است
 به طوری که بتوان هم از ابتدای صف و هم از انتهای صف حذف یا اضافه کرد و دسترسی داشت.
 این را برای این اضاقه کردم که بتوان راجت تر با طرف سمت چپ نوار
 کار کرد چون در غیر اینصورت کد به مشکل میخورد
 
 '''

def initialize_tape(input_string):
    """نوار ماشین تورینگ را با رشته ورودی مقداردهی می‌کند."""
    return deque(input_string)

def extend_tape_if_needed(tape, head_position):
    """اگر هد از نوار خارج شود، نوار را با نماد '$' گسترش می‌دهد."""
    if head_position < 0:
        tape.appendleft('$')
        head_position = 0
    elif head_position >= len(tape):
        tape.append('$')
    return head_position

def execute_transition(tape, head_position, current_state, transition_rules):
    """یک انتقال را اجرا می‌کند و حالت جدید، نماد جدید و جهت حرکت را برمی‌گرداند."""
    head_position = extend_tape_if_needed(tape, head_position)
    current_symbol = tape[head_position]
    transition_key = (current_state, current_symbol)

    if transition_key in transition_rules:
        new_state, new_symbol, direction = transition_rules[transition_key]
        tape[head_position] = new_symbol
        head_position += 1 if direction == 'R' else -1
        return new_state, head_position, True
    else:
        return current_state, head_position, False

def run_turing_machine(input_string, transition_rules, final_states, max_steps=1000):
    """ماشین تورینگ را اجرا می‌کند و نتیجه را برمی‌گرداند."""
    tape = initialize_tape(input_string)
    head_position = 0
    current_state = 'q0'
    step_counter = 0

    while step_counter < max_steps:
        step_counter += 1
        print(f"Step {step_counter}: Tape: {''.join(tape)}, Head: {head_position}, State: {current_state}")

        if current_state in final_states:
            print("String accepted!")
            return

        current_state, head_position, transition_success = execute_transition(tape, head_position, current_state, transition_rules)
        if not transition_success:
            print("String rejected (no transition found).")
            return

    print("String rejected (max steps reached).")


# تعریف رشته ورودی، قوانین انتقال و حالت‌های نهایی
#مثال اول برای رشته ای که پذیرش میشود

input_string = "1110"
transition_rules = {
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', '$'): ('q1', '1', 'L'),
    ('q1', '0'): ('q2', '1', 'L'),
    ('q1', '1'): ('q1', '0', 'L'),
    ('q1', '$'): ('q2', '1', 'L'),
}
final_states = {'q2'}

#مثال دوم برای حالتی که پذیرش نمی شود

'''input_string = "0001"
transition_rules = {
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', '$'): ('q1', '1', 'L'),
    ('q1', '0'): ('q2', '1', 'L'),
    # انتقالی برای ('q1', '1') وجود ندارد
    ('q1', '$'): ('q2', '1', 'L'),
}'''


final_states = {'q2'}

# اجرای ماشین تورینگ
run_turing_machine(input_string, transition_rules, final_states)