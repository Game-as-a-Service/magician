import {
  expect, test 
} from 'vitest'
import { helloFunction } from '@/components/hello.js'

test('hello test', () => {
  expect(helloFunction()).toBe('Hello World')
})