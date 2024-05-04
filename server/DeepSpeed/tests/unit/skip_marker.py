# Copyright (c) 2023 Habana Labs, Ltd. an Intel Company
# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

hpu_skip_tests = {}

g1_skip_tests = {
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_scatter_halftype":
    "FP16 datatype is not supported by Gaudi.",
    "unit/runtime/test_autocast.py::TestAutoCastDisable::test_missing_amp_autocast[True]":
    "FP16 datatype is not supported by Gaudi.",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[noCG-fp16-marian]":
    "FP16 datatype is not supported by Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-j-6B]":
    "FP16 datatype is not supported by Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-125m]":
    "FP16 datatype is not supported by Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[EleutherAI/gpt-neo-125M]":
    "FP16 datatype is not supported by Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[bigscience/bloom-560m]":
    "FP16 datatype is not supported by Gaudi.",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test_odd_world_size[fp16-marian]":
    "FP16 datatype is not supported by Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype0-True-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype2-False-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype2-True-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype0-False-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[True]":
    "Stuck",
    "unit/runtime/half_precision/test_bf16.py::TestZeroSupportedClientOptimizer::test[FusedAdam]":
    "Skipping test due to segfault. SW-170285",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Skipping test due to segfault then stuck. SW-174912",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Skipping test due to segfault then stuck. SW-174912",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Skipping test due to segfault then stuck. SW-174912",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp32]":
    "FusedAdam test not supported. Test got stuck.",
}

g2_skip_tests = {
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype0-True-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-False-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-True-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype2-False-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype2-True-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype0-False-True]":
    "Skipping test due to segfault. SW-170285",
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[True]":
    "Stuck",
    "unit/runtime/half_precision/test_bf16.py::TestZeroSupportedClientOptimizer::test[FusedAdam]":
    "Skipping test due to segfault. SW-170285",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Skipping test due to segfault then stuck. SW-174912",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Skipping test due to segfault then stuck. SW-174912",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Skipping test due to segfault then stuck. SW-174912",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp32]":
    "FusedAdam test not supported. Test got stuck.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp32]":
    "FusedAdam test not supported. Test got stuck.",
}

gpu_skip_tests = {
    "unit/runtime/zero/test_zero.py::TestZeroOffloadOptim::test[True]":
    "Disabled as it is causing test to stuck. SW-163517.",
}
