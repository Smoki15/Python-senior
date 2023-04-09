def helper(work):
    work_in_memory = work

    def helper(work):
        return f"I will help you with ypur {work_in_memory}. Afterwards I will help you with {work}"

    return helper


result = helper("homework")

print(result("cleaning"))
print(result("driving"))