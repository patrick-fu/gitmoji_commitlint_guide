# Gitmoji Commitlint Guide

## [English](README.md) | [中文](README_zh.md)

This repository demonstrate how to install commitlint and use Gitmoji as the Git Commit specification.

## Environmental dependence

npm@10.22 or higher.

## Note

The following `Commit Specification` paragraph is recommended to be copied to the `README` of your project repository,
and then the installation steps please refer to the paragraph `CommitLint Install Steps`.

## Commit Specification

> You need to execute `npm install` in this project root directory to install `commitlint`, `husky` tools (used to standardize Git commit messages).

This project uses [Gitmoji](https://gitmoji.dev) as the Git commit message specification, and the rules are as follows:

```txt
emoji subject(#ID)
BLANK LINE
Message Body
BLANK LINE
Footer
```

The specific rules are as follows:

1. Commit Message must start with an actual emoji UTF-8 character (not gitmoji code).
2. **A Commit does only one thing** (A simple criterion is that the title of the Commit Message must be able to fully summarize all the changes in this commit)
3. Header is required. It is recommended to use English, capitalize the first letter, and do not add a period at the end of the Header sentence; Body and Footer can be omitted.
4. Header must contain only one type. Please refer to [Gitmoji](https://gitmoji.dev) for the available types.
5. The header length should be between **15** and **100** characters.
6. If Commit resolves the issue, please end with (#ID) at the end of the header, and then close the Issue in the Body.
7. Use Markdown grammar to write in the body.
8. The verb uses the general present tense. ("Add feature" instead of "Added feature")
9. Use imperative grammar. ("Move cursor to..." instead of "Moves cursor to...")
10. Explain "what", "why" and "how" in the body.
11. All WIP (Work In Progress) Commits must have WIP 🚧 Emoji.

```sh
# Good
🙈 Update the project root .gitignore file
🏗 Enable bitcode for iOS
🚧 Add temporary testing code
```

Each Gitmoji has its specific meaning, such as `✨ -> Introduce new features`, `📝 -> Add or update documentation`, `🐛 -> Fix a bug`

Please choose the appropriate one according to what you did in the commit Gitmoji

> It is recommended to install the Gitmoji App or plug-in for easy search and copy emoji. (You can also click to copy emoji directly on the web page)

- [All related tools](https://gitmoji.dev/related-tools)

1. [Gitmoji App for macOS / Windows / Linux](https://github.com/patrick-fu/GitmojiApp)

    It is recommended to install this app on desktop.

    ![gitmojiapp.png](./gitmojiapp.png)

2. [Gitmoji Web page](https://gitmoji.dev)

    After the search box is filtered (for example, search `feat` to filter out the corresponding ✨ Gitmoji)

    Click the corresponding Gitmoji icon to directly copy the emoji to the clipboard.

3. [Gitmoji Plugin for Chrome](https://github.com/johannchopin/gitmoji-browser-extension)

4. [Gitmoji Plugin for VSCode](https://github.com/vtrois/gitmoji-vscode)

## CommitLint Install Steps

1. Execute the following commands in the repo root directory to install node dependent libraries and generate `package.json` and `package-lock.json` files. (You need to commit these two files to git, then other developers only need to execute `npm install`)

    ```sh
    npm install --save-dev @commitlint/{config-conventional,cli} husky
    ```

    > Remember to add the `node_modules` directory to `.gitignore` after installation

2. Execute the following commands in the repo root directory to initialize husky and create a husky (git hook) configuration file. This step will generate a `.husky/commit-msg` file, which also needs to be committed to git. This step is to execute commitlint when hook git commit.

    ```sh
    npx husky install

    npx husky add .husky/commit-msg "npx --no -- commitlint --edit ${1}"
    ```

3. Modify the `.husky/pre-commit` file automatically generated by husky. During the execution of `husky install` in the previous step, husky will automatically create this file for users to modify by themselves. The default is to execute `npm test`. For non-npm-managed projects, In other words, there is no need to execute this command, you can delete this file directly, or you can perform any operation you want to perform pre commit, such as performing a unit test. For example, change to the following:

    ```sh
    #!/bin/sh
    . "$(dirname "$0")/_/husky.sh"

    git fetch origin --prune --prune-tags # Pull Origin's latest submission and prune local redundant tags
    python3 ./run.py # Execute the build script, if the build fails (such as sys.exit(1) in the middle), the commit will be aborted
    ```

4. Add a hook to install husky in `package.json`. It is recommended to add `husky install` in the `scripts` field of your project root package json, so that when someone executes `npm install`, the husky hook will be installed automatically.

    ```json
    // package.json
    {
        "scripts": {
            "prepare": "husky install"
        }
    }
    ```

5. Modify the configuration of commitlint to the Gitmoji specification mentioned above. Add a `.commitlintrc.js` file in the root directory of the project with the following content. You can copy the file from this repository to your repository directory and submit it to git.

    ```js
    // The following emoji array is obtained from this json,
    // you may need to add the latest emoji to this array yourself
    // https://github.com/carloscuesta/gitmoji/blob/master/src/data/gitmojis.json
    const gitmojis = [
    '🎨','⚡️','🔥','🐛','🚑','✨','📝','🚀','💄','🎉',
    '✅','🔒','🔖','🚨','🚧','💚','⬇️','⬆️','📌','👷',
    '📈','♻️','➕','➖','🔧','🔨','🌐','✏️','💩','⏪',
    '🔀','📦','👽','🚚','📄','💥','🍱','♿️','💡','🍻',
    '💬','🗃','🔊','🔇','👥','🚸','🏗','📱','🤡','🥚',
    '🙈','📸','⚗','🔍','🏷️','🌱','🚩','🥅','💫','🗑',
    '🛂','🩹','🧐','⚰️'
    ];

    module.exports = {
    // Default rule: config-conventional
    // https://github.com/conventional-changelog/commitlint/tree/master/%40commitlint/config-conventional#rules
    extends: ['@commitlint/config-conventional'],
    parserPreset: {
        parserOpts: {
        // We change the parser regex pattern to match emoji UTF-8 character
        // The "[\u23ea-\ufe0f]{1,2}" means that some emojis are in two bytes but not one
        // So this pattern matchs string like "🐛 Fix a bug"
        headerPattern: /^([\u23ea-\ufe0f]{1,2})(?:\(([\w\$\.\-\* ]*)\))? (.*)$/,
        headerCorrespondence: ['type', 'scope', 'subject']
        }
    },
    rules: {
        'type-enum': [2, 'always', gitmojis],
        'type-case': [0, 'always', 'lower-case'],
        'subject-full-stop': [2, 'never', '.'],
        'subject-case': [2, 'always', 'sentence-case'],
        'header-min-length': [2, 'always', 15],
        'header-max-length': [2, 'always', 100],
        'body-max-line-length': [2, 'always', 200],
    }
    };
    ```

6. After the above steps are completed and committed && pushed to git remote, it is recommended to add a script to detect the `commitlint` node module in the **build script** of the project or other places where developers must pass (such as Xcode's PreBuild RunScript Build Phases, etc.) to make sure that all members of the project team have `commitlint` installed. This repository provides a simple script that can be hung in your build script. For details, please refer to `./run.py`

7. After completion, you can self-test whether it is effective. When the committed message does not meet the specifications, the operation will be aborted and an error message will be displayed, for example:

    ```blank
    ➜  gitmoji_commitlint_guide git:(master) ✗ git commit -m "📝 Update"
    ⧗   input: 📝 Update
    ✖   header must not be shorter than 15 characters, current length is 9 [header-min-length]

    ✖   found 1 problems, 0 warnings
    ⓘ   Get help: https://github.com/conventional-changelog/commitlint/#what-is-commitlint

    husky - commit-msg hook exited with code 1 (error)
    ➜  gitmoji_commitlint_guide git:(master) ✗
    ➜  gitmoji_commitlint_guide git:(master) ✗ git commit -m "Update README.md"
    ⧗   input: Update README.md
    ✖   subject may not be empty [subject-empty]
    ✖   type may not be empty [type-empty]

    ✖   found 2 problems, 0 warnings
    ⓘ   Get help: https://github.com/conventional-changelog/commitlint/#what-is-commitlint

    husky - commit-msg hook exited with code 1 (error)
    ➜  gitmoji_commitlint_guide git:(master) ✗
    ➜  gitmoji_commitlint_guide git:(master) ✗ git commit -m "📝 Update README.md"
    [master 8a186ca] 📝 Update README.md
    1 file changed, 1 insertion(+)
    ➜  gitmoji_commitlint_guide git:(master) ✗
    ```
