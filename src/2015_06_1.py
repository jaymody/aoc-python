solve = __import__("2015_06_common").solve

print(
    solve(
        on_fn=lambda _: 1,
        off_fn=lambda _: 0,
        toggle_fn=lambda x: 0 if x == 1 else 1,
    )
)
