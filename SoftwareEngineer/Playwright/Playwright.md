From [https\://learning.oreilly.com/course/playwright-testing-with/9781808728419/](https://learning.oreilly.com/course/playwright-testing-with/9781808728419/)

# Setup

## First project

To create a blank test project:

```
npm init playwright@latest
```

to run the test

```
npx playwright test
```

to see the report, there should be a playwright-report html file at the root or run:

```
npx playwright show-report
```

See in action with a ui. This ui shows every step

```
npx playwright test --ui
```

## ESLint

It is recommended to install the VS code extension ESLint. Also execute the following command which will install it on all project.

```
npm install -g eslint
```

Initialize ESLint on the project

```
npx eslint --init
```

# Core Concepts Browser, Context, Page, Fixtures

## Fixtures \- Page, Context, Browser

A **page** is a fresh tab in a fresh browser and is only accessible in the test:

```js
import { test, expect } from "@playwright/test";

test("has title", async ({ page }) => {
  await page.goto("https://playwright.dev/");

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/Playwright/);
});
```

A **context** is an isolated browser session, which can create pages. Cookies and local storage are owned by the context, so two page of the same context share the same Cookies and local storage.

```js
import { test, expect } from "@playwright/test";

test("has title on two page", async ({ context }) => {
  const page1 = await context.newPage();
  const page2 = await context.newPage();

  await page1.goto("https://playwright.dev/");
  await page2.goto("https://playwright.dev/");

  await expect(page1).toHaveTitle(/Playwright/);
  await expect(page2).toHaveTitle(/Playwright/);
});
```

The **browser** always to create multiple context with separate cookies and local storage.

```js
import { test, expect } from "@playwright/test";

test("has title on two browser process", async ({ browser }) => {
  const context1 = await browser.newContext();
  const context2 = await browser.newContext();

  const page1 = await context1.newPage();
  const page2 = await context2.newPage();

  await page1.goto("https://playwright.dev/");
  await page2.goto("https://playwright.dev/");

  await expect(page1).toHaveTitle(/Playwright/);
  await expect(page2).toHaveTitle(/Playwright/);
});
```

Those three lambda parameter are related to each other, so by default, we get one page of a context of a browser:

```js
import { test } from "@playwright/test";

test("lambda parameters", async ({ page, context, browser }) => {
  console.log(page.context() == context); // true
  console.log(browser == context.browser()); // true
});
```

## Structure of a Spec File

**test.describe** groups the tests

```js
// @ts-check
import { test, expect } from "@playwright/test";

test.describe("Example of grouping", () => {
  test("has title on a page", async ({ page }) => {
    ...
  });

  test("has title on two page", async ({ context }) => {
    ...
  });

  test("has title on two browser process", async ({ browser }) => {
    ...
  });

  test("lambda parameters", async ({ page, context, browser }) => {
    ...
  });
});
```

In the ui, the test are grouped:  
![](./images/Picture1.png)

## Before and After Hooks

There are after and before hooks:

- **test.beforeAll** is executed before all tests of the same worker
- **test.beforeEach** is executed before each test
- **test.afterEach** is executed after each test
- **test.afterAll** is executed after all tests of the same worker

For instance we can use the beforeEach to go to the page we want to test.

```js
// @ts-check
import { test, expect } from "@playwright/test";

test.describe("Example of grouping", () => {
  test.beforeAll(async () => {
    ...
  });

  test.beforeEach(async () => {
    await page.goto("http://localhost:3000/");
  });

  test.afterEach(async () => {
    ...
  });

  test.afterAll(async () => {
    ...
  });

  test("has title on a page", async ({ page }) => {
    ...
  });

  test("has title on two page", async ({ context }) => {
    ...
  });
});
```

## Test steps

test.step simply groups a test into logical steps. It is convenient to add a small title to each logical step.

```js
import { test, expect } from "@playwright/test";

test("has title on two page", async ({ page }) => {
  await test.step("navigate", async () => {
    await page.goto("https://playwright.dev/");
  });

  await test.step("assert", async () => {
    await expect(page).toHaveTitle(/Playwright/);
  });
});
```

# Test runner basics

## Tags

use tag to annotate the tests. For instance, we can annotate them by feature so we can run the relevant test if the feature is impacted. To add tags, simply add “@\<tagName\>” at the end of the title of a test.

Some rules:

- keep number of tags short. Do not add a tag for every bug.
- put tags at the end of the test title. Do not add tags behind a helper function.
- group test of the same feature inside the same folder

```js
// @ts-check
import { test, expect } from "@playwright/test";

test.describe("tags", () => {
  test("test 1 @test1", async ({ page }) => {
    ...
  });

  test("test 2", { tag: ["@test2"] }, async ({ page }) => {
    ...
  });
});
```

## VS code test explorer

To change the testing folder, go to the test tab, and scroll to the configuration to choose an alternative `playwright.config.js`

It is also possible to run the tests on other browsers, if they are configured in the `playwright.config.js`.

We can also show the browser while the test is running.

Running a test step-by-step is also possible, in debug mode by using the red mark on the left.

In watch mode, changing a test makes the test re-running.

## Running playwright command

From the folder were the config file is, we can run the following command to run all tests:

```
npx playwright test
```

running one spec file, is done by pointing at the spec file from the config file folder. Mind the / iso \\:

```
npx playwright test tests/example.spec.js
```

running all test in a folder, is very similar:

```
npx playwright test tests
```

running with the test name. \-g stands for grep. it will run any test containing this string after \-g.

```
npx playwright test -g "has title on two page"
```

Running one tag:

```
npx playwright test --grep @test1
npx playwright test --grep "@test1|@test2"
```

We can ask to view the browser with \--headed. It is advised to run one test.

```
npx playwright test --headed tests/example.spec.js
```

to run with one browser

```
npx playwright test --project=chromium
```

to have only one worker:

```
npx playwright test --workers=1
```

debug mode:

```
npx playwright test tests/example.spec.js --debug
```

## Annotations

We can **skip** a test by adding skip in the test. it can be in a test with a condition.  
**fixme** does the same.  
**test.slow()**, marks a test as slow and triple the timeout time.  
**only** will skip all other of the group.  
the **annotation** object contains a list or one annotation object with two properties “type” and “description”.

```js
// @ts-check
import { test, expect } from "@playwright/test";

test.describe("annotations", () => {
  test.skip("test 1", async ({ page }) => {
    ...
  });

  test.fixme("test 2", async ({ page }) => {
    ...
  });

  test("test 3", async ({ page }) => {
    ...
  });

  test("test 4", async ({ page }) => {
    test.slow();
    ...
  });

  test.only("test 5", async ({ page }) => {
    ...
  });

  test("test 6", async ({ page }) => {
    test.skip(browserName == "firefox", "not supported");
    ...
  });

  test(
    "test 7",
    {
      annotation: {
        type: "issue",
        description: "test-suite",
      },
    },
    async ({ page }) => {
      await page.goto("https://playwright.dev/");

      // Expect a title "to contain" a substring.
      await expect(page).toHaveTitle(/Playwright/);
    },
  );
});
```

## Reporter

The html page which opens is the reporter. We can change its configuration in the playwright.config.js, in the reporter property.  
See doc [https\://playwright.dev/docs/test-reporters](https://playwright.dev/docs/test-reporters)

We can change this report. It can be a list, a json, an html, junit (xml), …

```js
// @ts-check
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  ...
  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: [
    ["list"],
    ["html"],
    ["junit", { outputFile: "./junit-report/result.xml" }],
  ],
  ...
});
```

## npm custom script

Of course, you can add the test in the script part of the package.json.

```json
{
  ...
  "scripts": {
    "test": "playwright test",
    "test-ui": "playwright test --ui"
  },
  ...
}
```

# Locators

## getByRole and strict mode

A locator like `page.getByRole` aims to locate and return a DOM element in a page.

Playwright has a strict mode that forces each locator call to resolve to exactly one DOM element, if the function chaining `expect` is expecting one element. We can enforce to take the first encountered if we follow the locator by `.first()`.

The `page.getByRole()` locator reflects how users and assistive technology perceive the page, for example whether some element is a button or a checkbox. When locating by role, you should usually pass the accessible name as well, so that the locator pinpoints the exact element.

You can access the accessibility tab in the browser to find the Role and its name:

![](./images/Picture2.png)

```js
import { expect, test } from "@playwright/test";

test.describe("sample suite", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("http://localhost:3000/isolation-test.html");
  });

  test("test getByRole", async ({ page }) => {
    await expect(
      page.getByRole("button", { name: "Submit form" }),
    ).toBeVisible();
  });
});
```

## More getBy locators

`getByLabel` points to the DOM element which label is given as argument.

`getByPlaceholder` points to the DOM element which place-holder is given as argument.

For instance:

```js
page.getByLabel("Name:");
page.getByPlaceholder("Enter your full name (e.g., John Doe)");
page.getByText("Name:");
page.getByAltText("Form icon");
page.getByTitle("Please enter your full name");
page.getByTestId("name-input");
page.locator("#name-1");
```

find respectively:

- the `input` element which label is "Names:". It does not find the `label` elements.
- the `input` element because it has the given `Enter your full name (e.g., John Doe)` place holder
- the `label` element because its text inside is `Name:`
- the `img` element because its alternative text is `Form icon`
- the `input ` element because its title is `Please enter your full name`
- the `input ` element because its `data-testid` is `name-input:`
- the `input ` element because its css locator can be `#name-1` because its id is `#name-1`

```html
<div class="form-group" role="group">
  <img src="" alt="Form icon" />
  <label for="name-1">Name:</label>
  <input
    id="name-1"
    data-testid="name-input"
    placeholder="Enter your full name (e.g., John Doe)"
    title="Please enter your full name"
  />
</div>
```

## Filtering and chaining locators

When a locator resolves to multiple DOM element, we can use the `filter()` method to narrow down the locators. When the using a another locator method like `getByRole` after another locator, we look for another DOM element inside.

For instance, the following test:

- starts by finding the unordered list with its test id
- inside the unordered list, it finds the element that have the text "Practice test isolation"
- inside this list item, we can finf the `toggle` button.

```js
import { expect, test } from "@playwright/test";

test.describe("sample suite", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("http://localhost:3000/isolation-test.html");
  });

  test("filtering and chaining locators", async ({ page }) => {
    const todoList = page.getByTestId("todo-list");
    await expect(todoList).toBeVisible();

    const secondTodo = todoList
      .getByRole("listitem")
      .filter({ hasText: "Practice test isolation" });
    await expect(secondTodo).toBeVisible();

    const togleButton = secondTodo.getByRole("button", { name: "Toggle" });
    await expect(togleButton).toBeVisible();
  });

  test("test two @smoke", async ({ page }) => {});
});
```

```html
<ul data-testid="todo-list">
  <li>
    <span>Learn Playwright testing</span>
    <button>Toggle</button>
    <button>Delete</button>
  </li>

  <li>
    <span>Practice test isolation</span>
    <button>Toggle</button>
    <button>Delete</button>
  </li>
</ul>
```

# Reading & writing UI data

## Typing and Keyboard

The goal here is to explain how to interact with the keyboard. The first think to do is to focus on the element we want to writing in. We can use the locator `focus` or `click` method. Once the focus is achieved, we can write with use `page.keyboard` to get the keyboard and use `type` to write something or `press` to press key strokes. Alternatively, we can directly use the locator to `fill` the element with a text.

The following example shows the different possibilities:

```js
import { expect, test } from "@playwright/test";

test.describe("sample suite", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("http://localhost:3000/isolation-test.html");
  });

  test("Copy-paste example", async ({ page }) => {
    const email = "gatien.debast@gmail.com";
    const nameField = page.getByRole("textbox", { name: "Name:" });
    await nameField.focus();
    await page.keyboard.type(email);
    await page.keyboard.press("Control+A");
    await page.keyboard.press("Control+C");
    const mailField = page.getByRole("textbox", { name: "Email:" });
    await mailField.focus();
    await page.keyboard.press("Control+V");
  });

  test("fill form and submit example", async ({ page }) => {
    const nameField = page.getByRole("textbox", { name: "Name:" });
    await nameField.fill("Gatien De Bast");
    const mailField = page.getByRole("textbox", { name: "Email:" });
    await mailField.focus();
    await page.keyboard.type("gatien.debast@gmail.com");
    const submitButton = page.getByRole("button", { name: "Submit" });
    await submitButton.click();
  });
});
```

## Text retrieval methods

To get the static text in a the DOM, we can use the `textContent`, `innerText`, `allTextContents` and `allInnerTexts` methods.

```js
test("data retrival", async ({ page }) => {
  const titleElt = page.getByRole("heading", { name: "Form Submission" });
  await expect(titleElt).toBeVisible();
  console.log(await titleElt.textContent());
  console.log(await titleElt.innerText());
  console.log(await titleElt.allTextContents());
  console.log(await titleElt.allInnerTexts());
});
```

To get the value in an input field, we use `inputValue`:

```js
test("data writting and retrival", async ({ page }) => {
  const name = "Gatien De Bast";
  const nameField = page.getByRole("textbox", { name: "Name:" });
  await nameField.fill(name);
  const inputValue = await nameField.inputValue();
  expect(inputValue).toEqual(name);
});
```

## getting rows and cell in tables

We can use the `nth` from a locator to get the n-th element statisfying a locator.

This can be usefull to get the rows and the cell of a table:

```js
test("retriving table data", async ({ page }) => {
  const addButton = page.getByRole("button", { name: "Add new table row" });
  await addButton.click();
  const table = page.getByRole("table", { name: "Data Table" });
  const firstRow = table.getByRole("rowgroup", { name: "data" }).nth(0);
  const firstCell = firstRow.locator("td").nth(0);
  const value = await firstCell.textContent();
  expect(value).toBeTruthy();
});
```
