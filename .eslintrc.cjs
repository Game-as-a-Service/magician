module.exports = {
  root: true,
  env: {
    node: true,
    browser: true,
    'vue/setup-compiler-macros': true
  },
  extends: [
    'plugin:vue/vue3-recommended'
  ],
  overrides: [
    {
      files: [
        '**/?(*.)test.[jt]s?(x)'
      ],
      env: {
        jest: true
      }
    }
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-unused-vars': 'error',
    // 不連續空格
    'no-multi-spaces': 'error',
    // 空2格
    'indent': [ 'error', 2 ],
    // 物件空格 {   a:b   } => { a:b }
    'object-curly-spacing': [ 'error', 'always' ],
    // 物件換行
    'object-curly-newline': [ 'error', {
      'multiline': true, 'minProperties': 2, 'consistent': true 
    } ],
    // 括號去除空格 foo(   'bar'   ) =>  foo('bar');
    'space-in-parens': [ 'error', 'never' ],
    // 物件前後只有一個空格{ 'foo'  :    42 } => { 'foo': 42 };
    'key-spacing': [ 'error', { mode: 'strict' } ],
    // 逗號前后的空格  [1,     2,  3  ,4] => [1, 2, 4, 4]
    'comma-spacing': [ 'error', {
      'before': false, 'after': true 
    } ],
    // array 内使用空格 [ 1,2   ] => [ 1,2 ]
    'array-bracket-spacing': [ 'error', 'always' ],
    // if else 風格
    'brace-style': [ 'error', '1tbs' ],
    // function 後面要空格 
    'space-before-function-paren': [ 'error', 'always' ],
    // call 函数空格 fn  () => fn()
    'func-call-spacing': [ 'error', 'never' ],
    // 關鍵字前後空格 if ()
    'keyword-spacing': [ 'error', {
      'overrides': {
        'if': {
          'after': true, before: false 
        },
        'else': {
          'after': true, before: true 
        },
      }
    } ],
    // 物件取值不能有空格 obj  .  foo => obj.foo
    'no-whitespace-before-property': 'error',
    // 最大連續空行数
    'no-multiple-empty-lines': [ 'error', {
      'max': 1, 'maxEOF': 0, 'maxBOF': 0 
    } ],
    // 去除前後空行
    'padded-blocks': [ 'error', 'never' ],
    // 操作符是否空格 a=0 => a = 0
    'space-infix-ops': 'error',
    // 操作符空格 + -
    'space-unary-ops': 'error',
    // 箭頭函数空格 ()=>{}  => () => {}
    'arrow-spacing': [ 'error', {
      'before': true, 'after': true 
    } ],
    // 解構不空白 {... f} => {...f}
    'rest-spread-spacing': 'error',
    // 字串中空格 `${ fo }`
    'template-curly-spacing': [ 'error', 'always' ],
    // 禁止重複的 import
    'no-duplicate-imports': 'error',
    // 注解空一格 //a => // a
    'spaced-comment': [ 'error', 'always' ],
    // 使用單引號，字串中可以包含了一個其它引號 "a string containing 'single' quotes"
    quotes: [ 'error', 'single', { 'avoidEscape': true } ],
    semi: [ 'error', 'never' ],
    'eol-last': [ 'error', 'never' ],
    'vue/order-in-components': [ 'error', {
      order: [
        'el',
        'name',
        'key',
        'parent',
        'functional',
        [ 'delimiters', 'comments' ],
        [ 'components', 'directives', 'filters' ],
        'extends',
        'mixins',
        [ 'provide', 'inject' ],
        'ROUTER_GUARDS',
        'layout',
        'middleware',
        'validate',
        'scrollToTop',
        'transition',
        'loading',
        'inheritAttrs',
        'model',
        [ 'props', 'propsData' ],
        'emits',
        'setup',
        'asyncData',
        'data',
        'fetch',
        'head',
        'computed',
        'watch',
        'watchQuery',
        'LIFECYCLE_HOOKS',
        'methods',
        [ 'template', 'render' ],
        'renderError'
      ]
    } ],
    'vue/require-prop-types': 'error',
    'vue/require-default-prop': 'error',
    'vue/this-in-template': [ 'error', 'never' ],
    'vue/html-self-closing': [
      'error', {
        html: {
          void: 'never',
          normal: 'never',
          component: 'never'
        },
        svg: 'never',
        math: 'never'
      }
    ],
    'vue/component-name-in-template-casing': [ 'error', 'PascalCase', {
      registeredComponentsOnly: true,
      ignores: [ '/^router-/', '/^keep-/', '/^transition/', '/^component/' ]
    } ],
    // vue 檔案名稱需要為多字
    'vue/multi-word-component-names': [ 'error', {
      ignores: [ 'index' ]
    } ],
    // script setup 變數自動 return 所以不一定需要使用
    // deprecated
    'vue/script-setup-uses-vars': 'error',
    'vue/key-spacing': [ 'error', {
      beforeColon: false, afterColon: true 
    } ],
    // 物件換行
    'vue/object-property-newline': 'error',
    'vue/object-curly-spacing': [ 'error', 'always' ],
    'vue/padding-line-between-blocks': [ 'error', 'always' ],
    'vue/prefer-separate-static-class': [ 'error' ],
    'vue/comment-directive': 'off'
  }
}