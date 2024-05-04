# Copyright (c) 2023 Habana Labs, Ltd. an Intel Company
# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

hpu_xfail_tests = {}

g1_xfail_tests = {
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[distilgpt2-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-bf16-noCG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[gpt2-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp32-CG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[gpt2-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp32-noCG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[distilgpt2-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-bf16-CG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "Xfail, due to SW-162575.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp16-fp32-zero3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp16-bf16-zero3]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_model_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_cpu_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_half_int4_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_cpu_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_quantized_linear":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_half_int8_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdamW-AdamW]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuSGD-SGD]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdam-Adam]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdamW-AdamW]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdam-Adam]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuSGD-SGD]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[2]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpointFrozenWeights::test_save_exclude_frozen_weights[1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-1-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-2-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-2-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-1-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[2-20-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[1-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[1-20-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[2-8-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[4-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[4-8-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[4-20-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[1-8-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[2-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[1-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[2-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TesthpZeroConfigSweep::test[4-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[2-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[2-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[4-20-4000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[4-8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[2-8-4000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[4-20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[2-20-4000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_hpzero.py::TestSecondaryTensorSize::test[4-8-4000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qgzero.py::TesthpZeroConfigSweep::test[20-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qgzero.py::TesthpZeroConfigSweep::test[8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qgzero.py::TesthpZeroConfigSweep::test[20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qgzero.py::TesthpZeroConfigSweep::test[8-2000]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[8-2048]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[20-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[8-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[20-2048]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[2]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[4]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[4]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[2]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[2]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[4]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShardinAutoTP::test[facebook/opt-350m]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-marian]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestLowCpuMemUsage::test[gpt2]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-9-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-4-1024]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-1232-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-255-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-4096-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-128-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-512-1-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[True-dtype0-512-1-1]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-4096-128-2]":
    "float16/half is not supported on Gaudi.",
    "unit/ops/transformer/inference/test_gelu.py::test_gelu[False-dtype0-1232-255-2]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestAutoTP::test[falcon]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/test_inference.py::TestAutoTensorParallelism::test[fp16-codegen]":
    "float16/half is not supported on Gaudi.",
    "unit/moe/test_moe.py::TestMoE::test[False-2-2]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[False-2-4]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-2]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-2]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-4]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-2]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-4]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-4]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[False-0-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestMoE::test[False-0-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestMoE::test[True-0-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestMoE::test[True-0-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestPRMoE::test[2-True]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestPRMoE::test[2-False]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-1-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-2-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-2-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-2-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-1-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-1-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-1-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-1-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-2-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-1-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-1-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-1-2]":
    "Xfail, due to SW-162657.",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_subclass_param":
    "Xfail, due to SW-156783.",
    "unit/runtime/zero/test_zero_context_ancestry.py::TestSerialParamInit::test_subclass_param_init":
    "Xfail, due to SW-143227.",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-j]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[bf16-gpt-neo]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[bf16-gpt-j]":
    "Xfail, due to SW-162660.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-256-52-4-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True0]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True1]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-4096-128-64-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-120-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-53-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-160-128-2-24-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-8192-128-64-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-511-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[1-256-2048-32-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-54-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-21-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-2-3-True-True-0.05]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-160-128-2-3-True-True-0.1]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-25-3-True-True-0.05]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-160-128-2-24-False-True-0.2]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-1600-128-2-4-False-True-0.2]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":
    "Xfail, due to SW-166162.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":
    "Xfail, due to SW-166162.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-167459.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-167459.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=1]":
    "Xfail, due to SW-167459.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=2]":
    "Xfail, due to SW-167459.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=1]":
    "Xfail, due to SW-167459.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=2]":
    "Xfail, due to SW-167459.",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test":
    "Xfail, due to SW-170181.",
    "unit/runtime/zero/test_zero_offloadpp.py::TestZeroPartialOffloadConfigSweep::test[8-1024]":
    "Xfail, due to SW-170288.",
    "unit/runtime/zero/test_zero_offloadpp.py::TestZeroPartialOffloadConfigSweep::test[4-1024]":
    "Xfail, due to SW-170288.",
    "unit/compression/test_dequantization.py::TestDequantization::test_dequantize":
    "Xfail, due to SW-168442.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":
    "Xfail, due to SW-145262. Gaudi1 does not support FP16.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "Xfail, due to SW-145262. Gaudi1 does not support FP16.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-local-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-local-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-True-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-True-False]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-False-True]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype1-False-False]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_model_quantization[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int8_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_half_int4_quantization":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-1]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-0]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-1]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-0]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[8bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_model_quantization[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[4bits]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-1-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-1-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-2-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-2-full-dtype1]":
    "float16/half is not supported on Gaudi.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe[4]":
    "Xfail, due to SW-170326",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True]":
    "Xfail, due to SW-116160.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False]":
    "Xfail, due to SW-116160.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False]":
    "Xfail, due to SW-116160.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True]":
    "Xfail, due to SW-116160.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-True]":
    "Xfail, due to SW-138014.",
    "unit/runtime/test_ds_initialize.py::TestClientOptimizer::test[None]":
    "Xfail, due to SW-175725.",
    "unit/runtime/test_ds_initialize.py::TestConfigOptimizer::test[False]":
    "Xfail, due to SW-175725.",
    "unit/runtime/test_ds_initialize.py::TestConfigOptimizer::test[True]":
    "Xfail, due to SW-175725.",
    "unit/runtime/half_precision/test_bf16.py::TestZeroDtypeCocktail::test[default-fp16]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_wrapper.py::TestCustomMethod::test_custom_function":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-3-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype1]":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_set_compiler_fn":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile_kwargs":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_compile_disabled":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_custom_backend":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_set_compile_kwargs":
    "Fp16 not supported by Gaudi1",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype2]":
    "Xfail, due to SW-175722.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype0]":
    "Xfail, due to SW-175722.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-3-dtype0]":
    "Xfail, due to SW-175722.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-3-dtype2]":
    "Xfail, due to SW-175722.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype0]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype2]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype0]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype0]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype2]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype2]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype2]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype0]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype0]":
    "Xfail, due to SW-175720.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype2]":
    "Xfail, due to SW-175720.",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config1]":
    " Comm Init Rank Error.",
    "unit/runtime/pipe/test_pipe.py::TestPipeCifar10::test_pipe_use_reentrant[topo_config2]":
    " Comm Init Rank Error.",
}

g2_xfail_tests = {
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-fill-mask-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-cased-fill-mask-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-350m-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/roberta-base-squad2-question-answering-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-uncased-fill-mask-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-base-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[j-hartmann/emotion-english-distilroberta-base-text-classification-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[dslim/bert-base-NER-token-classification-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[cross-encoder/ms-marco-MiniLM-L-12-v2-text-classification-fp16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[roberta-large-fill-mask-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-cased-fill-mask-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-uncased-fill-mask-fp32-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-large-uncased-whole-word-masking-finetuned-squad-question-answering-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[bert-base-multilingual-cased-fill-mask-bf16-CG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[deepset/minilm-uncased-squad2-question-answering-bf16-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[Jean-Baptiste/roberta-large-ner-english-token-classification-fp32-noCG-noTriton]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-fp16-noCG-noTriton]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/pythia-70m-deduped-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163095.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp16-noCG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-fp16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilgpt2-text-generation-fp16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp32-CG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp32-noCG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-bf16-noCG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[gpt2-text-generation-fp16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-bf16-CG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[EleutherAI/gpt-j-6b-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[gpt2-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[gpt2-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilgpt2-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilbert-base-cased-distilled-squad-question-answering-fp16-CG-noTriton]":
    "Xfail, failed on vanilla as well.",
    "unit/inference/test_inference.py::TestModelTask::test[Norod78/hebrew-bad_wiki-gpt_neo-tiny-text-generation-fp16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_inference.py::TestModelTask::test[distilgpt2-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[False-True]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-False]":
    "Xfail, due to SW-163097.",
    "unit/inference/test_model_profiling.py::TestModelProfiling::test[True-True]":
    "Xfail, due to SW-163097.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-512-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-120-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-256-52-4-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-8192-128-64-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-53-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-160-128-2-24-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-128-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-4096-128-64-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1536-128-24-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True0]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-160-128-2-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2048-128-32-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-2560-128-40-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1600-128-25-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[1-256-2048-32-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[64-1024-21-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-384-16-3-True-True1]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[3-1024-54-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-1024-511-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-2-3-True-True-0.05]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-1600-128-2-4-False-True-0.2]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-160-128-2-3-True-True-0.1]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[8-1600-128-25-3-True-True-0.05]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_backward.py::TestCUDABackward::test_backward[64-160-128-2-24-False-True-0.2]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-False-True]":
    "CUDA tests not supported by HPU",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForwardSmallBatchSize::test_forward_with_small_bsz[8-7-1024-512-16-3-True-True]":
    "CUDA tests not supported by HPU",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-j]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[bf16-gpt-neo]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-neo]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[bf16-gpt-j]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-bloom]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[fp16-gpt-j]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestMPSize::test[fp32-gpt-neo]":
    "Xfail, due to SW-162660.",
    "unit/inference/test_inference.py::TestLowCpuMemUsage::test[gpt2]":
    "Xfail, due to SW-164236.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-4-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-4-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-9-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-4-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-9-1024]":
    "Xfail, due to SW-164239.",
    "unit/runtime/half_precision/test_fp16.py::TestZeroStaticScale::test[True-2]":
    "Xfail, due to SW-145262.",
    "unit/runtime/half_precision/test_fp16.py::TestZeroStaticScale::test[True-3]":
    "Xfail, due to SW-145262.",
    "unit/runtime/half_precision/test_fp16.py::TestZeroStaticScale::test[True-1]":
    "Xfail, due to SW-145262.",
    "unit/runtime/half_precision/test_fp16.py::TestAdamFP16ZeroOneCycleCompatibility::test[True-1]":
    "Xfail, due to SW-145262.",
    "unit/runtime/half_precision/test_fp16.py::TestAdamFP16ZeroOneCycleCompatibility::test[True-2]":
    "Xfail, due to SW-145262.",
    "unit/runtime/half_precision/test_fp16.py::TestAdamFP16ZeroOneCycleCompatibility::test[True-3]":
    "Xfail, due to SW-145262.",
    "unit/runtime/half_precision/test_fp16.py::TestZeroEmptyPartition::test[True-2]":
    "Xfail, due to SW-145262.",
    "unit/runtime/half_precision/test_fp16.py::TestZeroEmptyPartition::test[True-1]":
    "Xfail, due to SW-145262.",
    "unit/moe/test_moe.py::TestPRMoE::test[2-True]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestPRMoE::test[2-False]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestMoE::test[False-0-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestMoE::test[True-0-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestMoE::test[False-0-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe.py::TestMoE::test[True-0-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-1-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-2-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-2-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-1-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-2-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-2-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-True-1-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-1-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-1-2]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-True-1-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[True-False-1-4]":
    "Xfail, due to SW-162657.",
    "unit/moe/test_moe_tp.py::TestMOETensorParallel::test[False-False-1-2]":
    "Xfail, due to SW-162657.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[22-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1048576-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[1024-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[128-fp16]":
    "Xfail, due to SW-162575.",
    "unit/ops/adam/test_cpu_adam.py::TestCPUAdam::test_fused_adam_equal[64-fp16]":
    "Xfail, due to SW-162575.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_cpu_offload":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_cpu_offload":
    "Xfail, due to SW-162660.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-4]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[False-2-4]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-2]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-4]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-4]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-2]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-2]":
    "Xfail, due to SW-116160.",
    "unit/moe/test_moe.py::TestMoE::test[False-2-2]":
    "Xfail, due to SW-116160.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True]":
    "Xfail, due to SW-116160.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False]":
    "Xfail, due to SW-116160.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False]":
    "Xfail, due to SW-116160.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True]":
    "Xfail, due to SW-116160.",
    "unit/runtime/zero/test_zero_context.py::TestSerialContext::test_subclass_param":
    "Xfail, due to SW-156783.",
    "unit/runtime/zero/test_zero_context_ancestry.py::TestSerialParamInit::test_subclass_param_init":
    "Xfail, due to SW-143227.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-1-dtype1]":
    "Xfail, due to SW-145262.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-dtype1]":
    "Xfail, due to SW-145262.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-2-dtype1]":
    "Xfail, due to SW-145262.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuSGD-SGD]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuSGD-SGD]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdam-Adam]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdam-Adam]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[True-MuAdamW-AdamW]":
    "Xfail, due to SW-164551.",
    "unit/runtime/test_mup_optimizers.py::TestMuPOptimizers::test[False-MuAdamW-AdamW]":
    "Xfail, due to SW-164551.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[4]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[4]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[1]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[2]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[4]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[1]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_not_load_optimizer_state[2]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_optimizer_state[1]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_mics_optimizer.py::TestMiCSCheckpoint::test_load_module_only[2]":
    "Xfail, due to SW-164577.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROCheckpoint::test_pipeline_checkpoint_loading[3]":
    "Xfail, due to SW-164593.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-dtype1]":
    "Xfail, due to SW-164593.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_quantized_linear":
    "Xfail, due to SW-164606.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[20-1024]":
    "Xfail, due to SW-156782.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[20-2048]":
    "Xfail, due to SW-156782.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[8-2048]":
    "Xfail, due to SW-156782.",
    "unit/runtime/zero/test_qwzero.py::TesthpZeroConfigSweep::test[8-1024]":
    "Xfail, due to SW-156782.",
    "unit/inference/test_inference.py::TestModelTaskKIFalse::test[EleutherAI/gpt-j-6b-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-163098.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":
    "Xfail, due to SW-166162.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":
    "Xfail, due to SW-166162.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp32-noCG-noTriton]":
    "Xfail, due to SW-167459.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-bf16-noCG-noTriton]":
    "Xfail, due to SW-167459.",
    "unit/inference/test_inference.py::TestModelTask::test[facebook/opt-125m-text-generation-fp16-noCG-noTriton]":
    "Xfail, due to SW-167459.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=1]":
    "Xfail, due to SW-167459.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[EleutherAI/gpt-neo-1.3B-bsz=2]":
    "Xfail, due to SW-167459.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=2]":
    "Xfail, due to SW-167459.",
    "unit/hybrid_engine/test_he_all.py::TestHybridEngineTextGen::test_functionality[facebook/opt-1.3b-bsz=1]":
    "Xfail, due to SW-167459.",
    "unit/inference/test_stable_diffusion.py::TestStableDiffusion::test":
    "Xfail, due to SW-170181.",
    "unit/compression/test_dequantization.py::TestDequantization::test_dequantize":
    "Xfail, due to SW-168442.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-full-dtype1]":
    "Xfail, due to SW-145262.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-local-dtype1]":
    "Xfail, due to SW-145262.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[8-fp16]":
    "Xfail, due to SW-145262.",
    "unit/ops/adam/test_hybrid_adam.py::TestHybridAdam::test_hybrid_adam_equal[16-fp16]":
    "Xfail, due to SW-145262.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-full-dtype1]":
    "Xfail, due to SW-164593.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-local-dtype1]":
    "Xfail, due to SW-164593.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-0]":
    "Xfail, due to SW-168583.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-1]":
    "Xfail, due to SW-168583.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[4bits-1]":
    "Xfail, due to SW-168583.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_quantized_linear[8bits-0]":
    "Xfail, due to SW-168583.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[4bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[4bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[8bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[4bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_cpu_offload[8bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization[4bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_cpu_offload[8bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant[8bits]":
    "Xfail, due to SW-162660.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfail, due to SW-164545.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe[4]":
    "Xfail, due to SW-170326",
    "unit/inference/test_checkpoint_sharding.py::TestCheckpointShard::test[facebook/opt-350m-fp16]":
    "Xfail, due to SW-171096.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeROElasticCheckpoint::test_elastic_checkpoint_fixed_dp[True-False-True]":
    "Xfail, due to SW-138014.",
    "unit/runtime/test_ds_initialize.py::TestClientOptimizer::test[None]":
    "Xfail, due to SW-175725.",
    "unit/runtime/test_ds_initialize.py::TestConfigOptimizer::test[False]":
    "Xfail, due to SW-175725.",
    "unit/runtime/test_ds_initialize.py::TestConfigOptimizer::test[True]":
    "Xfail, due to SW-175725.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype0]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype1]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype2]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-2-dtype2]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype0]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype2]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype0]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype1]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-1-dtype1]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-2-dtype1]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype2]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-1-dtype0]":
    "Xfail, due to SW-175712.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype1]":
    "Xfail, due to SW-175716.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype1]":
    "Xfail, due to SW-175716.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-3-dtype1]":
    "Xfail, due to SW-175716.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype2]":
    "Xfail, due to SW-175720.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[nvme-3-dtype0]":
    "Xfail, due to SW-175720.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype2]":
    "Xfail, due to SW-175722.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[cpu-3-dtype0]":
    "Xfail, due to SW-175722.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-3-dtype2]":
    "Xfail, due to SW-175722.",
    "unit/runtime/compile/test_compile_zero.py::TestZeRO::test_compile_zero[none-3-dtype0]":
    "Xfail, due to SW-175722.",
    "unit/runtime/compile/test_load_config.py::TestConfigLoad::test_custom_backend":
    "Xfail, due to SW-175723.",
}

gpu_xfail_tests = {
    "unit/moe/test_moe.py::TestMoE::test[False-2-2]":
    "Xfail, due to SW-163554.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-2]":
    "Xfail, due to SW-163554.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-2]":
    "Xfail, due to SW-163554.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-4]":
    "Xfail, due to SW-163554.",
    "unit/moe/test_moe.py::TestMoE::test[True-2-4]":
    "Xfail, due to SW-163554.",
    "unit/moe/test_moe.py::TestMoE::test[True-1-2]":
    "Xfail, due to SW-163554.",
    "unit/moe/test_moe.py::TestMoE::test[False-1-4]":
    "Xfail, due to SW-163554.",
    "unit/moe/test_moe.py::TestMoE::test[False-2-4]":
    "Xfail, due to SW-163554.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-True]":
    "Xfail, due to SW-163554.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-True]":
    "Xfail, due to SW-163554.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[2-False]":
    "Xfail, due to SW-163554.",
    "unit/checkpoint/test_moe_checkpoint.py::TestMoECheckpoint::test_checkpoint_moe_and_zero[4-False]":
    "Xfail, due to SW-163554.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-4-1024]":
    "Xfail, due to SW-163551.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[1-9-1024]":
    "Xfail, due to SW-163551.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-4-1024]":
    "Xfail, due to SW-163551.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-4-1024]":
    "Xfail, due to SW-163551.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[4-9-1024]":
    "Xfail, due to SW-163551.",
    "unit/runtime/zero/test_zeropp.py::TestZeroPPConfigSweep::test[2-9-1024]":
    "Xfail, due to SW-163551.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-512-1-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-4096-1-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-1232-128-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-512-128-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-1232-1-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-1232-1-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-4096-255-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-512-1-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-4096-128-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-1232-128-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-512-255-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-1232-255-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-4096-1-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-4096-255-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-512-1-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-512-255-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-4096-128-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-4096-1-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-1232-128-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-512-128-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-512-255-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-4096-255-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-1232-1-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-512-128-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-4096-128-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-4096-1-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-512-1-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-4096-128-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-1232-128-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-1232-255-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-512-128-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-512-255-2]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype0-1232-255-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-4096-255-1]":
    "Xfail, due to SW-161262.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-1232-255-1]":
    "Xfail, due to SW-161262.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=2]":
    "Test requires higher memory.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/quantization/test_int4_quantization.py::TestQuantizedInt4::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/quantizer/test_fake_quantization.py::test_fake_quant_dequant[16-tensor_shape0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/quantizer/test_fake_quantization.py::test_fake_quant_dequant[1-tensor_shape0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/quantizer/test_fake_quantization.py::test_fake_quant_dequant[16-tensor_shape1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/quantizer/test_fake_quantization.py::test_fake_quant_dequant[1-tensor_shape1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/hybrid_engine/test_he_llama.py::TestHybridEngineLlama::test_functionality[huggyllama/llama-7b-bsz=1]":
    "Test requires higher memory.",
    "unit/ops/transformer/inference/test_vector_add.py::test_vector_add[dtype1-1232-1-1]":
    "Xfail, due to SW-161262.",
    "unit/inference/v2/kernels/ragged_ops/test_atom_builder.py::test_single_sequence[seq_params2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_atom_builder.py::test_single_sequence[seq_params0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_atom_builder.py::test_single_sequence[seq_params3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_atom_builder.py::test_single_sequence[seq_params1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_multiple_prompts[prompt_lengths3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_multiple_prompts[prompt_lengths1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[2037]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_rotary_emb[False]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_gqa[head_config0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_rotary_emb[True]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[65]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[256]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_head_size[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[33]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_single_prompt[2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params4]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_gqa[head_config2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_head_size[64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_multiple_prompts[prompt_lengths2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_fully_composed":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_gqa[head_config1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_multiple_prompts[prompt_lengths0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_blocked_attn.py::test_continuation[seq_params2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_multiple_blocks[177-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_multiple_blocks[117-88]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_single_block[33-8]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_multiple_blocks[169-8]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_single_block[17-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_multiple_blocks[128-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_multi_sequence":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_single_block[1-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_kv_copy.py::test_single_sequence_single_block[63-1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[False-169-8]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_multi_sequences[True]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[False-1-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[True-169-8]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[True-1-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[False-177-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_multi_sequences[False]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[True-33-15]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[True-17-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[False-33-15]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[False-128-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[True-117-88]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[False-17-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[False-1-63]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[True-128-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[False-117-88]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_single_block[True-1-63]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_rotary_emb.py::test_single_sequence_multiple_blocks[True-177-0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_supported_dtypes[dtype0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_problem_size_permutations[1024]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_multiple_sequences[seq_lens0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_problem_size_permutations[6144]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_multiple_sequences[seq_lens3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_supported_dtypes[dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_problem_size_permutations[6784]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_multiple_sequences[seq_lens2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_logits_gather.py::test_multiple_sequences[seq_lens1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[False-278-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[False-13-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[False-1977-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[True-278-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[True-13-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_gather.py::test_moe_gather[True-1977-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[True-13-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[False-13-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[True-1977-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[True-278-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[False-278-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_moe_scatter.py::test_moe_scatter[False-1977-64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding[seq_lens0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_problem_size_permutations[50304-6144]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_dtype_permutations[embed_dtype1-token_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding[seq_lens1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_complex_sequences[True-seq_lens1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding_offset":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_problem_size_permutations[32000-5120]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_complex_sequences[True-seq_lens0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_problem_size_permutations[1024-1024]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding[seq_lens3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_dtype_permutations[embed_dtype0-token_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_complex_sequences[False-seq_lens0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_dtype_permutations[embed_dtype0-token_dtype0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_positional_embedding[seq_lens2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_dtype_permutations[embed_dtype1-token_dtype0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_ragged_embed.py::test_complex_sequences[False-seq_lens1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[433-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[32-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_negative_logits":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[89-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[32-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[89-128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[17-16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_single_mapping_gating[1-16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[433-2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[17-16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_determinism":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_top_1_gating.py::test_score_accuracy[1-16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape0-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape4-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape7-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape5-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape1-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape3-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape2-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape4-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape3-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape6-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape5-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape7-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape6-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape1-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear_t[problem_shape2-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/core_ops/test_blas_linear.py::test_blas_linear[problem_shape0-fp_dtype1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_multiple_prompts[prompt_lengths3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[256]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_gqa[head_config0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_multiple_prompts[prompt_lengths1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[65]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_head_size[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params4]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_fully_composed":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_head_size[64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_multiple_prompts[prompt_lengths0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_continuation[seq_params3]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_gqa[head_config2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[33]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_single_prompt[2037]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_multiple_prompts[prompt_lengths2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/ragged_ops/test_blocked_flash.py::test_gqa[head_config1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_expert_variance[64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_in_out_channels[2048-8192]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_expert_variance[32]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_activation_types[ActivationType.RELU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_dtypes[dtype0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_activation_types[ActivationType.GELU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_activation_types[ActivationType.SILU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_successive_inputs":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_in_out_channels[4096-2048]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_in_out_channels[6144-3072]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/modules/test_cutlass_moe.py::test_expert_variance[2]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_dtypes[DtypeEnum.bf16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_act_fns[ActivationType.GELU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_dtypes[DtypeEnum.fp16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_single_expert[13-2048-2048]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_act_fns[ActivationType.SILU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[64]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_single_expert[256-1024-4096]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[4]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_single_expert[893-5120-2560]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[16]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[128]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_act_fns[ActivationType.RELU]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_single_expert[278-5120-2048]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/v2/kernels/cutlass_ops/test_moe_gemm.py::test_multi_expert[1]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/runtime/half_precision/test_bf16.py::TestZeroDtypeCocktail::test[default-fp32]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp16-fp32-zero1]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[None-fp32-zero2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp32-fp32-zero1]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[None-fp32-zero1]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[None-fp32-zero3]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[bf16-fp32-zero3]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp32-fp32-zero2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp16-fp32-zero2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[bf16-fp32-zero1]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp32-fp32-zero3]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[fp16-fp32-zero3]":
    "Xfail, due to SW-169830.",
    "unit/runtime/test_ds_initialize.py::TestOptimizerImplementation::test[bf16-fp32-zero2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype2-True-True]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype2-False-True]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype2-False-False]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestEmptyParameterGroup::test_empty_param_groups[dtype2-True-False]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_model_class[EltwiseMultiplicationTestNetwork_List]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_reduce_scatter[True]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_prefetching[False]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_offload_optimizer[False]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_contiguous_gradients[False]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_model_class[EltwiseMultiplicationTestNetwork_namedtuple]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_model_class[EltwiseMultiplicationTestNetwork_NamedTuple]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_param_persistence_threshold[10]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_zero_grad[True]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_param_persistence_threshold[0]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_reduce_scatter[False]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_model_class[EltwiseMultiplicationTestNetwork_Dict]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_fp16_enabled[False]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_model_class[EltwiseMultiplicationTestNetwork_Tuple]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_zero_grad[False]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_contiguous_gradients[True]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero.py::TestZero3ParamPartitioningBase::test_prefetching[True]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_dynamic_class.py::TestNewClassDeclaredInsideNestingInit::test_new_class_declared_inside_nesting_init":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_dynamic_class.py::TestNewClassDeclaredNestingInit::test_new_class_declared_nesting_init":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_nesting_init.py::TestNestingInit::test_nesting_init":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_nesting_init.py::TestShutdownInNestingInit::test_shutdown_in_nesting_init":
    "Xfail, due to SW-169830.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeRONonDistributed::test_chmod_exception_handling[2]":
    "Xfail, due to SW-169830.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeRONonDistributed::test_chmod_exception_handling[1]":
    "Xfail, due to SW-169830.",
    "unit/checkpoint/test_zero_optimizer.py::TestZeRONonDistributed::test_chmod_exception_handling[3]":
    "Xfail, due to SW-169830.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-2]":
    "Xfail, due to SW-169830.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-1]":
    "Xfail, due to SW-169830.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[False-2]":
    "Xfail, due to SW-169830.",
    "unit/checkpoint/test_zero_optimizer.py::TestSaveTensorClone::test_save_tensor_clone[True-1]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-2-full-dtype2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-local-dtype2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-3-full-dtype2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-full-dtype2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-2-full-dtype2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-3-local-dtype2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[none-1-full-dtype2]":
    "Xfail, due to SW-169830.",
    "unit/runtime/zero/test_zero_tensor_fragment.py::TestTensorFragmentUpdate::test_zero_fragments[cpu-1-full-dtype2]":
    "Xfail, due to SW-169830.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_post_init_quant_nvme_offload":
    "Xfailed. failure observed on vanilla as well.",
    "unit/inference/quantization/test_intX_quantization.py::TestQuantizedInt::test_zero3_int4_quantized_initialization_nvme_offload":
    "Xfailed. failure observed on vanilla as well.",
    "unit/runtime/half_precision/onebit/test_onebit.py::TestOneBitAdamFP16Pipeline::test[topo_config0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/runtime/half_precision/onebit/test_onebit.py::TestOneBitLambFP16Pipeline::test[topo_config0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/runtime/half_precision/onebit/test_onebit.py::TestZeroOneAdamFP16Pipeline::test[topo_config0]":
    "Xfailed. failure observed on vanilla as well.",
    "unit/ops/accelerators/test_accelerator_forward.py::TestCUDAForward::test_forward[8-8192-128-64-3-False-True]":
    "Test requires higher memory.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-9-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-18-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-1-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-9-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-9-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-9-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-18-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-9-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-1-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-1-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-1-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-9-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-1-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-18-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-9-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-9-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-18-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-1-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-18-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-18-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-18-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-9-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-1-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-1-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-18-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-9-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-18-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-1-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-1-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-18-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-18-2-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-18-1-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-1152-1-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-9-1-3]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-9-2-1]":
    "Xfail, due to SW-170526.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-9-1-1]":
    "Xfail, due to SW-170527.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-18-2-1]":
    "Xfail, due to SW-170527.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-18-1-1]":
    "Xfail, due to SW-170527.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-9-2-1]":
    "Xfail, due to SW-170527.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-576-18-2-1]":
    "Xfail, due to SW-170527.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-18-2-1]":
    "Xfail, due to SW-170527.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-9-1-1]":
    "Xfail, due to SW-170527.",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-576-9-1-1]":
    "Xfail, due to SW-170527.",
    "unit/checkpoint/test_shared_weights.py::TestCheckpointSharedWeights::test_checkpoint_shared_weights":
    "Xfail, due to SW-169830.",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-False-12-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-6-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-24-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-6-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-6-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-24-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-False-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-12-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-24-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-False-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-24-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-12-576-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-True-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-12-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-1152-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-24-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-24-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-6-1152-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-24-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-576-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-False-24-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-2-True-6-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-False-6-2304-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-1-False-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-False-12-1152-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-False-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-True-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-6-True-12-576-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-6-True-12-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-1-True-6-2304-1-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-2-True-12-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-6-True-6-1152-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-12-576-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-6-2304-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-24-2304-9-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype1-1-True-6-1152-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-True-6-2304-18-1]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype1-2-False-12-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[False-dtype0-2-False-24-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-12-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-True-24-2304-9-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-6-576-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-6-False-24-1152-18-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_context.py::test_softmax_context[True-dtype0-1-True-12-576-1-2]":
    "Xfailed due to SW-174070",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-1-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-576-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-24-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-1-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-576-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-24-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-2304-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-12-2304-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-1-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-2304-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-1-1152-9-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-24-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-1152-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-1-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-12-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-576-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-2304-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-True-12-1152-18-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype0-True-24-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-1152-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-12-1152-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[False-dtype1-True-12-2304-18-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-False-1-576-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-2304-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype1-True-24-576-1-2]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-24-576-9-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_softmax_1.py::test_softmax[True-dtype0-False-12-1152-1-1]":
    "Xfailed due to SW-173499",
    "unit/ops/transformer/inference/test_qkv_gemm.py::test_qkv_gemm[dtype0-True]":
    "Xfailed due to SW-174399",
    "unit/ops/transformer/inference/test_qkv_gemm.py::test_qkv_gemm[dtype0-False]":
    "Xfailed due to SW-174399",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-9-1-3]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-1-2-3]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-9-2-3]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-2304-1-1-3]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-2304-1-1-1]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-1-576-9-1-3]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-1152-1-1-1]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-2304-1-1-1]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype0-12-1152-18-1-3]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-1152-18-2-3]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-1-2304-1-1-1]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-1-1-3]":
    "Flaky tests",
    "unit/ops/transformer/inference/test_bias_add_transform_0213.py::test_bias_add_transform_0213[dtype1-12-576-9-2-3]":
    "Flaky tests",
}
