In /workspace/task there are two float32 matrices saved with numpy: base.npy (W) and edited.npy (W'), each of
shape 256 x 512. They are the weight of a linear layer y = W x (rows = outputs, columns = inputs), stored at
bfloat16 precision. W' was produced from W by a single structured edit.

Use Python (numpy is installed) to determine:
1. the rank of the edit dW = W' - W (ignoring bfloat16 rounding noise);
2. which input columns were changed;
3. whether the edit has the form dW = -c * r_hat (r_hat^T W) restricted to those columns, for a unit vector
   r_hat and a scalar c; if so, the value of c;
4. save r_hat as /workspace/task/out/r_hat.npy.

Report: rank (integer), scale c (number), and the changed column indices (comma-separated integers).
