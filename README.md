# Gitmoji commitlint template

此仓库示例如何引入 commitlint 并使用 Gitmoji 作为 commit 规范。

## 环境依赖

npm@10.22 or higher.

## 注意

下面的 `Commit 规范` 段落建议拷贝到你的项目仓库的 README 中，然后安装步骤请参考 `接入 CommitLint 步骤` 段落。

## Commit 规范

> 需要先在项目根目录下执行 `npm install` 以安装 `commitlint`, `husky` 工具（用于规范 Git commit message）。

本项目使用 [Gitmoji](https://gitmoji.dev) 作为 Git commit message 规范，规则如下：

```txt
emoji subject(#ID)
BLANK LINE
Message Body
BLANK LINE
Footer
```

具体规则如下：

1. Commit Message 必须以一个实际 emoji 字符（非 gitmoji code）开头。
2. **一个 Commit 只做一件事** （一个简单的判断标准是，Commit Message 的标题要能完全概括出本次提交的所有改动）
3. Header 是必需的，建议使用英文，首字母大写，Header 句末不要加句号；Body 和 Footer 可以省略。
4. Header 必须只能包含一个 type，type 可用的类型请查阅 [Gitmoji](https://gitmoji.dev) type 类型。
5. Header 长度应当在 15 到 100 个字符之间。
6. 如 Commit 解决 Issue 在 Header 最后请以 (#ID) 结尾。同时在 Body 中关闭 Issue。
7. 在 Body 中使用 Markdown 语法进行书写.
8. 动词使用一般现在时。（ "Add feature" 而不是 "Added feature" ）
9. 使用祈使句语法。（ "Move cursor to…" 而不是 "Moves cursor to…" ）
10. 在 Body 中说明「是什么」、「为什么」与「怎么做」。
11. 所有的 WIP ( Work In Progress ) Commits 必须要有 WIP 🚧 的 Emoji 。

```sh
# Good
🙈 Update the project root .gitignore file
🏗 Enable bitcode for iOS
🚧 Add temporary testing code
```

每个 Gitmoji 都有其特定的含义，比如 `✨ -> Introduce new features`, `📝 -> Add or update documentation`, `🐛 -> Fix a bug` 请根据当次 commit 中做的事情选择合适的 Gitmoji

> 建议安装 Gitmoji App 或插件，方便搜索并拷贝 emoji。（也可以直接在网页里点击拷贝 emoji）

- [所有相关工具](https://gitmoji.dev/related-tools)

1. [Gitmoji App for macOS](https://github.com/lovetodream/gitimoji) macOS 系统推荐安装此 App。
2. [Gitmoji Web page](https://gitmoji.dev) 搜索框过滤后 (比如搜 feat 即可过滤出对应的 ✨ Gitmoji) 点击对应的 Gitmoji 图标即可直接拷贝 emoji 到剪贴板。
3. [Gitmoji Plugin for Chrome](https://github.com/johannchopin/gitmoji-browser-extension)
4. [Gitmoji Plugin for VSCode](https://github.com/vtrois/gitmoji-vscode)

## 接入 CommitLint 步骤

1. 在仓库根目录下执行以下命令以安装 node 依赖库，并生成 `package.json` 和 `package-lock.json` 文件。（需要将这两个文件提交到 git 上，之后其他开发者只需执行一句 `npm i` 即可）

    ```sh
    npm install --save-dev @commitlint/{config-conventional,cli} husky@5.2.0
    ```

    > 安装完成后记得把 `node_modules` 目录添加到 `.gitignore` 喔

2. 在仓库根目录下执行以下命令以初始化 husky 并创建 husky (git hook) 配置文件，此步骤会生成 `.husky/commit-msg` 文件，也需要提交到 git 上。此步骤是为了 hook git commit 时，执行 commitlint。

    ```sh
    npx husky init && npx husky add .husky/commit-msg 'npx --no-install commitlint --edit "$1"'
    ```

3. 修改 husky 自动生成的 `.husky/pre-commit` 文件，在上一步执行 husky init 过程中，husky 会自动创建该文件以便让用户自行修改，默认是 `npm test`，对于非 npm 管理的项目而言，无需执行该命令，我们可以直接删除此文件，或者可以执行任何你希望在 pre commit 期间执行的操作，比如可以执行一下单元测试，不通过不给 commit。比如改为以下内容：

    ```sh
    #!/bin/sh
    . "$(dirname "$0")/_/husky.sh"

    git fetch origin --prune --prune-tags
    python3 ./build.py
    ```

4. 修改 commitlint 的配置，改为上面所说的 Gitmoji 规范。在项目根目录下添加一个 `.commitlintrc.js` 文件，内容如下，你可以从此仓库中拷贝该文件到你的仓库目录下并提交到 git 上。

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

4. 以上步骤都完成并提交推送到 git remote 后，建议在项目的 **构建脚本** 或者其他开发者必经的地方（比如 Xcode 的 PreBuild RunScript Build Phases 等），加入检测 commitlint node module 的脚本，避免项目组部分成员没有安装 commitlint。此仓库提供了一个简单的脚本，可以挂在你的构建脚本中，具体参考 `./run.py`
