from forloop import ForloopClient
from forloop.nodes import Start, NewVariable, OpenBrowser, LoadWebsite, Wait, ExtractXPath, MathModifyVariable, ConvertVariableType, StringModifyVariable

fc = ForloopClient(project_key="test_user@forloop.ai")

pipe1 = fc.new_pipeline('immobilier')

pipe1.add(Start())
pipe1.add(NewVariable(variable_name='empty', variable_value='https://www.immobilier.ch/en/buy/apartment-house/zurich/page-'))
pipe1.add(NewVariable(variable_name='link_id', variable_value=1))
pipe1.add(OpenBrowser(in_browser=True, driver='Firefox'))
pipe1.add(LoadWebsite(url='https://www.immobilier.ch/en/buy/apartment-house/zurich/page-1?t=sale', take_screenshot=False))
pipe1.add(Wait(milliseconds=10000, rand_ms=0))
extractxpath = pipe1.add(ExtractXPath(xpath='//div[@class="filter-item-container"]//a[contains(@id,"link-result-item")]//@href', output=fc.variables['newlink'], write_mode='w+', save_to='DataFrame', column='url', list_as_str=False))
pipe1.add(Wait(milliseconds=1000, rand_ms=0))
pipe1.add(MathModifyVariable(variable_name='link_id', math_operation='+', argument=1, new_variable_name='link_id'))
pipe1.add(ConvertVariableType(variable_name='link_id', variable_type='str', new_variable_name='newlink'))
pipe1.add(StringModifyVariable(variable_name='empty', string_operation='Concatenate', argument=fc.variables['newlink'], argument2='', new_variable_name='load_link'))
pipe1.add(StringModifyVariable(variable_name='newlink', string_operation='Concatenate', argument='_immobilier.txt', argument2='', new_variable_name='newlink'))
pipe1.add(LoadWebsite(url=fc.variables['load_link'], take_screenshot=False))
wait = pipe1.add(Wait(milliseconds=5000, rand_ms=0))

pipe1.add_edge(wait, extractxpath)
