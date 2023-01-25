from forloop import ForloopClient
from forloop.nodes import Start, NewVariable, OpenBrowser, LoadWebsite, Wait, ExtractXPath

fc = ForloopClient(project_key="test_user@forloop.ai")

pipe1 = fc.new_pipeline('immobilier')

pipe1.add(Start())
pipe1.add(NewVariable(variable_name='empty', variable_value='https://www.immobilier.ch/en/buy/apartment-house/zurich/page-'))
pipe1.add(NewVariable(variable_name='link_id', variable_value=1))
pipe1.add(OpenBrowser(in_browser=True, driver='Firefox'))
pipe1.add(LoadWebsite(url='https://www.immobilier.ch/en/buy/apartment-house/zurich/page-1?t=sale', take_screenshot=False))
pipe1.add(Wait(milliseconds=10000, rand_ms=0))
pipe1.add(ExtractXPath(xpath='//div[@class="filter-item-container"]//a[contains(@id,"link-result-item")]//@href', output=fc.variables['newlink'], write_mode='w+', save_to='DataFrame', column='url', list_as_str=False))
pipe1.add(Wait(milliseconds=1000, rand_ms=0))
