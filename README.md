# [GitHub Action Python Example](https://pypi.org/project/GitHub-Action-Python-Example/)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/louis70109/line-notify#contributing)

This is a GitHub Action example for an auto publish PyPi package and test automation.

## Setup PyPi property

- [Go PyPi](https://pypi.org/) ➡️ Your project ➡️ Account Setting.

![](https://nijialin.com/images/2021/action/token1.png)

- Create an API token.
  - Note: If you just first time create the token, need to select **all project** at Scope.

![](https://nijialin.com/images/2021/action/token2.png)

- You would find **username** and **password**.
- Setup **PYPI_USERNAME** and **PYPI_PASSWORD** in GitHub `Setting` ➡️ `Secrets`.
- Click _New repository secret_ and add two property.

![](https://nijialin.com/images/2021/action/token3.png)

- Modify `GitHub_Action_Python_Example/__version__.py` version number(e.g. 1.0.2).

- Click and draft `Release` note.

![](https://nijialin.com/images/2021/action/release1.png)

- `.github/workflows/publish.yml` will help you to publish package to PyPi.

![](https://nijialin.com/images/2021/action/release4.png)

## Install package

```
pip install GitHub-Action-Python-Example
```

```python
from GitHub_Action_Python_Example.client import HelloWorld

message = HelloWorld(message="Change the World~")
print(message.get_message())
```

# License

[MIT](https://github.com/louis70109/line-notify/blob/master/LICENSE) © [NiJia Lin](https://nijialin.com/about/)
