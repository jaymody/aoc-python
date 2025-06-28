solve = __import__("2015_06_common").solve

print(
    solve(
        on_fn=lambda x: x + 1,
        off_fn=lambda x: max(0, x - 1),
        toggle_fn=lambda x: x + 2,
    )
)
