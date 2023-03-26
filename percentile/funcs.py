import scipy

select_dist = Element("select-dist")
input_param = Element("input-param")
input_prob = Element("input-prob")
container_result = Element("container-result")


def calc(*args, **kwargs):
    if not select_dist.element.value:
        return None

    expression = "scipy.stats." + select_dist.element.value + ".ppf("
    expression += "q=" + input_prob.element.value + ", "
    expression += input_param.element.value + ")"

    message = expression + "<br/>"
    message += str(eval(expression))
    container_result.element.innerHTML = message

def display_param_event(e):
    if not select_dist.element.value:
        return None
    if select_dist.element.value == "norm":
        input_param.element.value = "loc=0, scale=1"
    if select_dist.element.value == "chi2":
        input_param.element.value = "df=10"
    if select_dist.element.value == "binom":
        input_param.element.value = "n=10, p=0.2"

select_dist.element.onchange = display_param_event
