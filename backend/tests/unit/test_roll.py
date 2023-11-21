import domain.spell


def test_fix_roll_dice_one(monkeypatch):
    dice_results = 666
    monkeypatch.setattr(domain.spell, "roll_dice", lambda: dice_results)

    for _ in range(1000):
        result = domain.spell.roll_dice()
        assert result == 666


def test_fix_roll_dice_multiple(monkeypatch):
    dice_results = [1, 3, 2, 2, 3]
    dice_results_iter = iter(dice_results)
    monkeypatch.setattr(domain.spell, "roll_dice", lambda: next(dice_results_iter))

    for i in range(len(dice_results)):
        result = domain.spell.roll_dice()
        assert result == dice_results[i]
