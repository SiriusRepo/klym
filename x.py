string = """
Ahhh yes! Now I see exactly 😄

Rule:

* Swap **each `l`** with the vowel **immediately before it**, if there is one.
* If there’s **no vowel before the `l`**, do nothing.

Apply to your examples:

* `label` → `lable` ✅ (`e` before `l`)
* `default` → `defalut` ✅ (`a` before `l`)
* `table` → stays `table` ❌ (no vowel immediately before `l`)

---

Applying to your full sentence:

Original:

> out of range? jump to the default label! otherwise, you can go to the jump table. In the end, jump to the return label.

Step by step:

* `default` → `defalut`
* `label` → `lable`
* `table` → `table` (unchanged)
* `label` → `lable`

✅ Final:

> out of range? jump to the defalut lable! otherwise, you can go to the jump table. In the end, jump to the return lable.

---

This fully respects the “swap with previous vowel only” rule.

If you want, I can **apply this to your whole assembly/jump table explanation** for a fun Klym-flavored version. Do you want me to do that?

"""

vowels = "aeiouAEIOU"
out = ""
for char in string:
    last = out[-1:]
    if last in vowels and char == 'l':
        out = out[:-1]
        out = out + char + last
    else:
        out = out + char

print(out)