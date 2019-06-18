import Control.Monad.State

-- https://wiki.haskell.org/The_Fibonacci_sequence#Monadic
fib n = flip evalState (0,1) $ do
  forM [0..(n-1)] $ \_ -> do
    (a,b) <- get
    put (b,a+b)
  (a,b) <- get
  return a

main = do
  let sumOfEvenFibs = sum $ filter even $ takeWhile (< 4000000) $ map fib [1..]
  print $ 4613732 == sumOfEvenFibs