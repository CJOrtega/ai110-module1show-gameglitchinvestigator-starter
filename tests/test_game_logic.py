from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug 1: New Game button — win outcome must be correctly identified so
# app.py can set status="won" and the New Game button can reset it.
def test_win_sets_correct_outcome():
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"


# Bug 2: Backwards hints — too-high guess must say go lower, not higher.
def test_too_high_hint_direction():
    _, message = check_guess(80, 50)
    assert "LOWER" in message

def test_too_low_hint_direction():
    _, message = check_guess(20, 50)
    assert "HIGHER" in message


# Bug 3: History not updating — parse_guess must return the correct value
# so that the right entry is appended to history on every guess.
def test_valid_guess_parsed_for_history():
    ok, value, err = parse_guess("37")
    assert ok is True
    assert value == 37
    assert err is None
