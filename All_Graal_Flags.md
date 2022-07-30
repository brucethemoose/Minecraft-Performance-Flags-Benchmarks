graalvm-ee-java17-22.2.0\bin>java -XX:+JVMCIPrintProperties --version
[JVMCI properties]
jvmci.Compiler = null                                                     [String]
          Selects the system compiler. This must match the getCompilerName() value returned by a jdk.vm.ci.runtime.JVMCICompilerFactory provider. An empty string or the value "null" selects a compiler that will raise an exception upon receiving a compilation request.
jvmci.InitTimer = false                                                  [Boolean]
          Specifies if initialization timing is enabled.
jvmci.ForceTranslateFailure = null                                        [String]
          Forces HotSpotJVMCIRuntime.translate to throw an exception in the context of the peer runtime. The value is a filter that can restrict the forced failure to matching translated objects. See HotSpotJVMCIRuntime.postTranslation for more details. This option exists soley to test correct handling of translation failure.
jvmci.PrintConfig = false                                                [Boolean]
          Prints VM configuration available via JVMCI.
jvmci.AuditHandles = false                                               [Boolean]
          Record stack trace along with scoped foreign object reference wrappers to debug issue with a wrapper being used after its scope has closed.
jvmci.TraceMethodDataFilter = null                                        [String]
          Enables tracing of profiling info when read by JVMCI.
          Empty value: trace all methods
          Non-empty value: trace methods whose fully qualified name contains the value.
jvmci.UseProfilingInformation = true                                     [Boolean]

[Graal properties]
graal.ASMInstructionProfiling = null                                      [String]
          Enables instruction profiling on assembler level. Valid values are a
          comma separated list of supported instructions. Compare with subclasses
          of Assembler.InstructionCounter.
graal.AbortOnBenchmarkCounterOverflow = false                            [Boolean]
          Abort VM with SIGILL if benchmark counters controlled by the
          (Generic|Timed|Benchmark)DynamicCounters
          option overflow.  WARNING: No descriptive error message will be printed! In
          case of an overflow, manual inspection of the emitted code is required.
graal.ActiveProcessorCount = -1                                          [Integer]
          Overwrites the available number of processors provided by the OS. Any
          value <= 0 means using the processor count from the OS.
graal.AggregatedMetricsFile = null                                        [String]
          File to which aggregated metrics are dumped at shutdown. A CSV format
          is used if the file ends with .csv otherwise a more human readable
          format is used. If not specified, metrics are dumped to the console.
graal.AliasArrayTypeFlows = true                                         [Boolean]
          Model all array type flows using a unique elements type flow
          abstraction.
graal.AllocationProfilingThreshold = 1048576                             [Integer]
          The minimum size in bytes required for printing an allocation profiling
          entry
graal.AllocationSiteSensitiveHeap = false                                [Boolean]
          A context sensitive heap means that each heap allocated object is
          modeled by using at least the allocation site.
graal.AlwaysInlineIntrinsics = false                                     [Boolean]
          Unconditionally inline intrinsics
graal.AlwaysInlineVTableStubs = false                                    [Boolean]
graal.AlwaysPreTouch = false                                             [Boolean]
          Force all freshly committed pages to be pre-touched
graal.AnalysisContextSensitivity = "insens"                               [String]
          Controls the static analysis context sensitivity. Available values:
          insens (context insensitive analysis), allocsens (context insensitive
          analysis, context insensitive heap, allocation site sensitive heap),
          _1obj (1 object sensitive analysis with a context insensitive heap),
          _2obj1h (2 object sensitive with a 1 context sensitive heap)
graal.AnalysisSizeCutoff = 8                                             [Integer]
          The maximum size of type and method profiles returned by the static
          analysis. -1 indicates no limitation.
graal.AnalysisStatisticsFile = null                                       [String]
          Analysis results statistics file.
graal.ArrayRegionEqualsConstantLimit = 4096                              [Integer]
          Array region equality checks will be evaluated at compile time if the
          receiver is a constant and its length is smaller than this value.
graal.AutomaticReferenceHandling := false                                [Boolean]
          Determines if the reference handling is executed automatically or
          manually.
graal.BaseTargetSpending = 120                                           [Integer]
          The base target spending used to estimate the inlining threshold; the
          higher, the likelier it is to inline.
graal.BenchmarkCounterPrintingCutoff = true                              [Boolean]
          Use a cutoff to print only most significant counters.
graal.BenchmarkCountersDumpDynamic = true                                [Boolean]
          Dump dynamic counters
graal.BenchmarkCountersDumpStatic = false                                [Boolean]
          Dump static counters
graal.BenchmarkCountersFile = null                                        [String]
          File to which benchmark counters are dumped. A CSV format is used if
          the file ends with .csv otherwise a more human readable format is used.
          The fields in the CSV format are: category, group, name, value
graal.BenchmarkDynamicCounters = null                                     [String]
          Turn on the benchmark counters. The format of this option is:

            (err|out),start pattern,end pattern

          Start counting when the start pattern matches on the given stream and stop when the end pattern occurs.
          You can use "~" to match 1 or more digits.
          Examples:

            err, starting =====, PASSED in
            out,Iteration ~ (~s) begins:,Iteration ~ (~s) ends:

          The first pattern matches DaCapo output and the second matches SPECjvm2008 output.

          As a more detailed example, here are the options to use for getting statistics
          about allocations within the DaCapo pmd benchmark:

            -XX:JVMCICounterSize=<value> -XX:-JVMCICountersExcludeCompiler \
            -Dgraal.BenchmarkDynamicCounters="err, starting ====, PASSED in " \
            -Dgraal.ProfileAllocations=true

          The JVMCICounterSize value depends on the granularity of the profiling -
          10000 should be sufficient. Omit JVMCICountersExcludeCompiler to exclude
          counting allocations on the compiler threads.
          The counters can be further configured by the ProfileAllocationsContext option.

          We highly recommend the use of -Dgraal.AbortOnBenchmarkCounterOverflow=true to
          detect counter overflows eagerly.
graal.BlindConstants = false                                             [Boolean]
          Blind constants in code with a random key.
graal.BootstrapInitializeOnly = false                                    [Boolean]
          Do not compile anything on bootstrap but just initialize the compiler.
graal.BootstrapTimeout = 15.0                                             [Double]
          Maximum time in minutes to spend bootstrapping (0 to disable this
          limit).
graal.BootstrapWatchDogCriticalRateRatio = 0.25                           [Double]
          Ratio of the maximum compilation rate below which the bootstrap
          compilation rate must not fall (0 or less disables monitoring).
graal.BouncyCastleIntrinsics = true                                      [Boolean]
          Enable native intrinsics for BouncyCastle.
graal.BreakChainedPhis = true                                            [Boolean]
          Break chained phis
graal.CallGraphCompilerNodeLimit = 35000                                 [Integer]
          Controls the maximum number of compiler nodes that can appear in the
          call graph
graal.CallGraphSizeLimit = 1200                                          [Integer]
          Controls the maximum size of the call graph before ceasing inlining.
graal.CallGraphSizePenaltyCoefficient = 0.001                             [Double]
          Reduces the likelihood of exploring call graph subtrees that are large.
graal.CanOmitFrame = true                                                [Boolean]
graal.CanonicalGraphStringsCheckConstants = false                        [Boolean]
          Exclude virtual nodes when dumping canonical text for graphs.
graal.CanonicalGraphStringsExcludeVirtuals = true                        [Boolean]
          Exclude virtual nodes when dumping canonical text for graphs.
graal.CanonicalGraphStringsRemoveIdentities = true                       [Boolean]
          Attempts to remove object identity hashes when dumping canonical text
          for graphs.
graal.ClearMetricsAfterBootstrap = false                                 [Boolean]
          Clear the debug metrics after bootstrap.
graal.CollectImageBuildStatistics = false                                [Boolean]
          Collect information during image build about devirtualized invokes and
          bytecode exceptions.
graal.CollectYoungGenerationSeparately = null                            [Boolean]
          Determines if a full GC collects the young generation separately or
          together with the old generation.
graal.CompilationBailoutAsFailure = false                                [Boolean]
          Treat compilation bailouts like compilation failures.
graal.CompilationCountLimit = 0                                          [Integer]
          The number of compilations allowed for any method before the VM exits
          (a value of 0 means there is no limit).
graal.CompilationExcludePhases = null                                     [String]
          Exclude certain phases from compilation, either unconditionally or with
          a method filter. Multiple exclusions can be specified separated by ':'.
          Phase names are matched as substrings, e.g.:
          CompilationExcludePhases=PartialEscape:Loop=A.*,B.foo excludes
          PartialEscapePhase from all compilations and any phase containing
          'Loop' in its name from compilations of all methods in class A and of
          method B.foo.
graal.CompilationExpirationPeriod = 300                                  [Integer]
          Time limit in seconds before a compilation expires (0 to disable the
          limit). A non-zero value for this option is doubled if assertions are
          enabled and quadrupled if DetailedAsserts is true.
graal.CompilationFailureAction = Silent                                   [String]
          Specifies the action to take when compilation fails.

          The accepted values are:
              Silent  - Print nothing to the console.
               Print  - Print a stack trace to the console.
            Diagnose* - Retry the compilation with extra diagnostics.
              ExitVM  - Same as Diagnose except that the VM process exits after retrying.

          * If "Diagnose" is set compilation will be retried with extra diagnostics enabled including dumping (see file:doc-files/DumpHelp.txt).
            In such a scenario DiagnoseDumpLevel can be used to specify the dump level (DebugContext dump levels) accordingly.

graal.CompilationIsolateAddressSpaceSize = 0                                [Long]
          Size of the reserved address space of each compilation isolate (0:
          default for new isolates).
graal.CompilationWatchDogStackTraceInterval = 60.0                        [Double]
          Interval in seconds between a watch dog reporting stack traces for long
          running compilations.
graal.CompilationWatchDogStartDelay = 0.0                                 [Double]
          Delay in seconds before watch dog monitoring a compilation (0 disables
          monitoring).
graal.CompileGraalWithC1Only = true                                      [Boolean]
          In tiered mode compile Graal and JVMCI using optimized first tier code.
graal.CompileInIsolates = true                                           [Boolean]
          Activate runtime compilation in separate isolates (enable support
          during image build with option SupportCompileInIsolates).
graal.CompileInPerThreadReusedIsolates = true                            [Boolean]
          Create one reusable isolate per compilation thread as opposed to one
          isolate per compilation (enable through CompileInIsolates).
graal.CompilerConfiguration = null                                        [String]
          Names the compiler configuration to use. If omitted, the compiler
          configuration with the highest auto-selection priority is used. To see
          the set of available configurations, supply the value 'help' to this
          option.
graal.CompilerNodePenaltyCoefficient = 0.006                              [Double]
          Controls the likelihood of exploring subtrees that already have a lot
          of code during inlining.
graal.ConcGCThreads = 0                                                  [Integer]
          Number of threads concurrent gc will use
graal.ConditionalElimination = true                                      [Boolean]
graal.ConditionalEliminationMaxIterations = 4                            [Integer]
graal.ConsiderVectorizableLoops = true                                   [Boolean]
          Consider the vectorizability of loop during the duplication of a merge
          inside a loop.There are rare cases where duplication can destroy
          vectorization.
graal.CostNewLiveVariable = 4                                            [Integer]
          PullThroughPhiOptimization: Abstract cost for the creation of a new
          live value: new values can have a negativeimpact on register
          allocation, therefore we penalize it.
graal.CostReductionFactor = 32.0                                          [Double]
          PullThroughPhiOptimization: Cost/Benefit heuristic for EE floating node
          duplication: reduce cost by a constant factor when comparing with
          relative benefit.
graal.Count = null                                                        [String]
          Pattern for specifying scopes in which counters are enabled. See the
          Dump option for the pattern syntax. An empty value enables all counters
          unconditionally.
graal.CountedStripMiningInnerLoopTrips = 4096                            [Integer]
          The max number of iterations the counted inner loop takes.
graal.CountedStripMiningLogCounters = false                              [Boolean]
          Print counter phi values on each outer and inner loop iteration.
graal.CountedStripMiningMinFrequency = 4                                 [Integer]
          Minimal frequency to consider a loop for strip mining.
graal.Counters = null                                                     [String]
          Comma separated names of counters that are enabled irrespective of the
          value for Count option. An empty value enables all counters
          unconditionally.
graal.CrashAt = null                                                      [String]
          Pattern for method(s) that will trigger an exception when compiled.
          This option exists to test handling compilation crashes gracefully. See
          the MethodFilter option for the pattern syntax. A ':Bailout' suffix
          will raise a bailout exception and a ':PermanentBailout' suffix will
          raise a permanent bailout exception.
graal.CrashAtIsFatal = false                                             [Boolean]
          Converts an exception triggered by the CrashAt option into a fatal
          error if a non-null pointer was passed in the _fatal option to
          JNI_CreateJavaVM. This option exists for the purpose of testing fatal
          error handling in libgraal.
graal.CutoffCodeSizePenaltyCoefficient = 1.0E-5                           [Double]
          Controls the likelihood of further exploring subtrees with a lot of
          code during inlining.
graal.DebugPeelingSynonyms = false                                       [Boolean]
          Debug simulation synonyms during simulation-based loop peeling.
graal.DebugStubsAndSnippets = false                                      [Boolean]
          Enable debug output for stub code generation and snippet preparation.
graal.DeoptALot = false                                                  [Boolean]
graal.DeoptAfterOSR = true                                               [Boolean]
          Deoptimize OSR compiled code when the OSR entry loop is finished if
          there is no mature profile available for the rest of the method.
graal.DeoptsToDisableOptimisticOptimization = 40                         [Integer]
graal.DetailedAsserts = false                                            [Boolean]
          Enable expensive assertions if normal assertions (i.e. -ea or -esa) are
          enabled.
graal.DetectInvertedLoopsAsCounted = true                                [Boolean]
graal.DiagnoseDumpLevel = 3                                              [Integer]
          Specify the dump level if CompilationFailureAction#Diagnose is used.See
          CompilationFailureAction for details.
          file:doc-files/CompilationFailureActionHelp.txt
graal.DiagnosticDetails = ""                                              [String]
          Specifies how many details are printed for certain diagnostic thunks,
          e.g.: 'DumpThreads:1,DumpRegisters:2'. A value of 1 will result in the
          maximum amount of information, higher values will print less
          information. By default, the most detailed output is enabled for all
          diagnostic thunks. Wildcards (*) are supported in the name of the
          diagnostic thunk.
graal.DisableExplicitGC = false                                          [Boolean]
          Ignore calls to System.gc()
graal.DisableIntercept = false                                           [Boolean]
          Disable intercepting exceptions in debug scopes.
graal.DisableIntrinsics = null                                            [String]
          Disable intrinsics matching the given method filter (see MethodFilter
          option for details). For example, 'DisableIntrinsics=String.equals'
          disables intrinsics for any method named 'equals' in a class whose
          simple name is 'String'. You can append ':verbose' at the end of the
          filter value to print out disabled intrinsics as they are encountered
          during compilation (e.g., 'String.equals:verbose').
graal.DivertParameterReturningMethod = true                              [Boolean]
          Analysis: Detect methods that return one of their parameters and
          hardwire the parameter straight to the return.
graal.DominatorUsageTreeMaxDepth = 16                                    [Integer]
graal.Dump = null                                                         [String]
          Filter pattern for specifying scopes in which dumping is enabled.

          A filter is a list of comma-separated terms of the form:

            <pattern>[:<level>]

          If <pattern> contains a "*" or "?" character, it is interpreted as a glob pattern.
          Otherwise, it is interpreted as a substring. If <pattern> is empty, it
          matches every scope. If :<level> is omitted, it defaults to 1. The term
          ~<pattern> is a shorthand for <pattern>:0 to disable a debug facility for a pattern.

          The default log level is 0 (disabled). Terms with an empty pattern set
          the default log level to the specified value. The last
          matching term with a non-empty pattern selects the level specified. If
          no term matches, the log level is the default level. A filter with no
          terms matches every scope with a log level of 1.

          Examples of debug filters:
          ---------
            (empty string)

            Matches any scope with level 1.
          ---------
            :1

            Matches any scope with level 1.
          ---------
            *

            Matches any scope with level 1.
          ---------
            CodeGen,CodeInstall

            Matches scopes containing "CodeGen" or "CodeInstall", both with level 1.
          ---------
            CodeGen:2,CodeInstall:1

            Matches scopes containing "CodeGen" with level 2, or "CodeInstall" with level 1.
          ---------
            Outer:2,Inner:0}

            Matches scopes containing "Outer" with log level 2, or "Inner" with log level 0. If the scope
            name contains both patterns then the log level will be 0. This is useful for silencing subscopes.
          ---------
            :1,Dead:2

            Matches scopes containing "Dead" with level 2, and all other scopes with level 1.
          ---------
            Dead:0,:1

            Matches all scopes with level 1, except those containing "Dead".   Note that the location of
            the :1 doesn't matter since it's specifying the default log level so it's the same as
            specifying :1,Dead:0.
          ---------
            Code*

            Matches scopes starting with "Code" with level 1.
          ---------
            Code,~Dead

            Matches scopes containing "Code" but not "Dead", with level 1.
graal.DumpAfterEveryBCI = false                                          [Boolean]
          Dump the current graph after every bci to IGV.
graal.DumpDetailedNodeTypeStats = false                                  [Boolean]
          Gather statistics on local variables and their lifetimes relative to
          FrameStates.
graal.DumpEndVersusExitLoopFrequencies = false                           [Boolean]
          Debug flag to dump loop frequency differences computed based on loop
          end or exit nodes.If the frequencies diverge a lot, this may indicate
          missing profiles on control flowinside the loop body.
graal.DumpHeapAndExit = false                                            [Boolean]
          Create a heap dump and exit.
graal.DumpMethodsData = false                                            [Boolean]
          Dump a JSON array containing all methods included in the image and
          exit.
graal.DumpOnError = false                                                [Boolean]
          Send compiler IR to dump handlers on error.
graal.DumpOnPhaseChange = null                                            [String]
          Dump a before and after graph if the named phase changes the
          graph.%nThe argument is substring matched against the simple name of
          the phase class
graal.DumpPath = "graal_dumps"                                            [String]
          The directory where various Graal dump files are written.
graal.DumpingErrorsAreFatal = false                                      [Boolean]
          Treat any exceptions during dumping as fatal.
graal.DuplicateALot = false                                              [Boolean]
          Perform Duplications as long as there is any sane improvement.
graal.DuplicationBudgetFactor = 0.25                                      [Double]
          Percentage in node cost graph size for the duplication budget. Computed
          relative to the methods code size.
graal.DuplicationBudgetFactorLate = 0.5                                   [Double]
          Percentage in node cost graph size for the late duplication budget.
          Computed relative to the methods code size.
graal.DuplicationCostReductionFactor = 64                                [Integer]
          Cost/Benefit heuristic for EE simulation-based code duplication: reduce
          cost by a constant factor when comparing with relative benefit.
graal.DuplicationMinBranchFrequency = 0.66                                [Double]
          Ignore low frequency branches during duplication.
graal.DynamicCountersPrintGroupSeparator = true                          [Boolean]
          Use grouping separators for number printing
graal.EagerSnippets := true                                              [Boolean]
          Eagerly construct extra snippet info.
graal.EarlyCodeEmissionOrder = false                                     [Boolean]
          Enable early code emission order computation instead of late code
          emission order computation
graal.EarlyGVN = false                                                   [Boolean]
          Perform early global value numbering.
graal.EarlyLICM = false                                                  [Boolean]
          Perform early loop invariant code motion.
graal.EmitStringSubstitutions = true                                     [Boolean]
          Emit substitutions for String methods
graal.EnableSignalHandling = false                                       [Boolean]
          Enables signal handling
graal.EnterpriseCloneReadElimination = true                              [Boolean]
          Try to eliminate array clone operations by handling clone operations in
          early read elimination.
graal.EnterpriseEarlyReadElimination = true                              [Boolean]
          Run more read eliminations early in the compilation pipeline.
graal.EnterprisePartialUnroll = true                                     [Boolean]
          Enable EE version of partial loop unrolling that considers more loop
          shapes for unrolling.
graal.EnterpriseRCELogRangeCheckValues = false                           [Boolean]
          Log all range check sub values to stdout.
graal.EnterpriseRangeCheckElimination = true                             [Boolean]
          Perform range check elimination for java long type range checks.
graal.ErgoHeapSizeLimit = 0                                                 [Long]
          Maximum ergonomically set heap size (in bytes); zero means use MaxRAM *
          MaxRAMPercentage / 100
graal.EscapeAnalysisIterations = 2                                       [Integer]
graal.EscapeAnalysisLoopCutoff = 20                                      [Integer]
graal.EscapeAnalyzeOnly = null                                            [String]
graal.ExactFullUnrollMaxNodes = 800                                      [Integer]
graal.ExactPartialUnrollMaxNodes = 200                                   [Integer]
graal.ExcludeFunctionFromDuplication = null                               [String]
          Exclude compilations that MethodFilter.match this string from the
          duplication optimization.
graal.ExhaustiveHeapScan = false                                         [Boolean]
          Scan all objects reachable from roots for analysis. By default false.
graal.ExitOnOutOfMemoryError = false                                     [Boolean]
          Exit on the first occurrence of an out-of-memory error that is thrown
          because the Java heap is out of memory.
graal.ExitVMOnException = false                                          [Boolean]
          Alias for CompilationFailureAction=ExitVM.
graal.ExpandAllProximityBonus = 6.0                                       [Double]
          The decrease in call graph expansion pressure when there are few call
          nodes left to explore.
graal.ExpandAllProximityBonusInertia = 2.0                                [Double]
          The inertia at which the expand-all proximity bonus decreases with the
          number of yet unexpanded nodes.
graal.ExpansionInertiaBaseValue = 550                                    [Integer]
          The slowness at which the expansion pressure grows with code size; the
          higher it is, the slower the pressure growth.
graal.ExpansionInertiaInvokeBonus = 14                                   [Integer]
          The extra slowness at which the expansion pressure grows with the code
          size, for each extra invoke node.
graal.ExpansionInertiaMax = 2000                                         [Integer]
          The max slowness at which the expansion pressure grows with the code
          size.
graal.ExplicitGCInvokesConcurrent = false                                [Boolean]
          A System.gc() request invokes a concurrent collection
graal.ExtendedAsserts = false                                            [Boolean]
          Enable extended asserts which slow down analysis.
graal.FailedLoopExplosionIsFatal = false                                 [Boolean]
          Do not bail out but throw an exception on failed loop explosion.
graal.FallbackExecutorRuntimeJavaArg = <string>*                         [Strings]
          Internal option used to specify runtime java arguments for
          FallbackExecutor.
graal.FlightRecorder = false                                             [Boolean]
          Enable Java Flight Recorder.
graal.FlightRecorderLogging = "all=warning"                               [String]
          Usage: -XX:FlightRecorderLogging=[tag1[+tag2...][*][=level][,...]]

          When this option is not set, logging is enabled at a level of WARNING.
          When this option is set to the empty string, logging is enabled at a level of INFO.
          When this option is set to "disable", logging is disabled entirely.

          Otherwise, this option expects a comma separated list of tag combinations, each with an optional wildcard (*) and level.
          A tag combination without a level is given a default level of INFO.
          Messages with tags that match a given tag combination are set to log at that tag combination's level.
          If a tag combination does not have a wildcard, then only messages with exactly the same tags are matched.
          Otherwise, messages whose tags are a subset of the tag combination are matched.
          Specifying "all" instead of a tag combination matches all tag combinations.
          If more than one tag combination matches a message's tags, the rightmost one will apply.
          Messages with tags that do not have any matching tag combinations are set to log at a default level of WARNING.
          This option is case insensitive.

          Available log levels:
          [trace, debug, info, warning, error, off]

          Available log tags:
          [jfr, system, event, setting, bytecode, parser, metadata, dcmd]
graal.FloatingDivNodes = true                                            [Boolean]
          Try to float non-constant division operations to expose global value
          numbering of divisions.
graal.ForceAdversarialLayout = false                                     [Boolean]
          Place N-byte constants in the data section such that they are
          misaligned with respect to N*2. For example, place 4 byte constants at
          offset 4, 12 or 20, etc. This layout is used to detect instructions
          that load constants with alignment smaller than the fetch size. For
          instance, an XORPS instruction that does a 16-byte fetch of a 4-byte
          float not aligned to 16 bytes will cause a segfault.
graal.ForceDumpGraphsBeforeCompilation = false                           [Boolean]
          Force-dump graphs before compilation
graal.ForceUnroll = false                                                [Boolean]
          Force partial unrolling of loops if at all possible.
graal.FrameStateLivenessStatistics = false                               [Boolean]
          Gather statistics on local variables and their lifetimes relative to
          FrameStates.
graal.FullUnroll = true                                                  [Boolean]
graal.FullUnrollAsPEACleanup = true                                      [Boolean]
          Perform full unrolling as a Partial Escape Analysis Cleanup
graal.FullUnrollConstantCompareBoost = 15                                [Integer]
graal.FullUnrollMaxApplication = 60                                      [Integer]
graal.FullUnrollMaxIterations = 600                                      [Integer]
graal.FullUnrollMaxNodes = 400                                           [Integer]
graal.G1ConcMarkStepDurationMillis = 10.0                                 [Double]
          Target duration of individual concurrent marking steps in milliseconds.
graal.G1ConcRSHotCardLimit = 4                                              [Long]
          The threshold that defines (>=) a hot card.
graal.G1ConcRSLogCacheSize = 10                                             [Long]
          Log base 2 of the length of conc RS hot-card cache.
graal.G1ConcRefinementGreenZone = 0                                         [Long]
          The number of update buffers that are left in the queue by the
          concurrent processing threads. Will be selected ergonomically by
          default.
graal.G1ConcRefinementRedZone = 0                                           [Long]
          Maximum number of enqueued update buffers before mutator threads start
          processing new ones instead of enqueueing them. Will be selected
          ergonomically by default.
graal.G1ConcRefinementServiceIntervalMillis = 300                           [Long]
          The last concurrent refinement thread wakes up every specified number
          of milliseconds to do miscellaneous work.
graal.G1ConcRefinementThreads = 0                                        [Integer]
          The number of parallel rem set update threads. Will be set
          ergonomically by default.
graal.G1ConcRefinementThresholdStep = 2                                     [Long]
          Each time the rset update queue increases by this amount activate the
          next refinement thread if available. The actual step size will be
          selected ergonomically by default, with this value used to determine a
          lower bound.
graal.G1ConcRefinementYellowZone = 0                                        [Long]
          Number of enqueued update buffers that will trigger concurrent
          processing. Will be selected ergonomically by default.
graal.G1ConfidencePercent = 50                                           [Integer]
          Confidence level for MMU/pause predictions.
graal.G1HeapWastePercent = 5                                             [Integer]
          Amount of space, expressed as a percentage of the heap size, that G1 is
          willing not to collect to avoid expensive GCs.
graal.G1MixedGCCountTarget = 8                                              [Long]
          The target number of mixed GCs after a marking cycle.
graal.G1PeriodicGCInterval = 0                                              [Long]
          Number of milliseconds after a previous GC to wait before triggering a
          periodic gc. A value of zero disables periodically enforced gc cycles.
graal.G1PeriodicGCInvokesConcurrent = true                               [Boolean]
          Determines the kind of periodic GC. Set to true to have G1 perform a
          concurrent GC as periodic GC, otherwise use a STW Full GC.
graal.G1PeriodicGCSystemLoadThreshold = 0.0                               [Double]
          Maximum recent system wide load as returned by the 1m value of
          getloadavg() at which G1 triggers a periodic GC. A load above this
          value cancels a given periodic GC. A value of zero disables this check.
graal.G1RSetRegionEntries = 0                                               [Long]
          Max number of regions for which we keep bitmaps. Will be set
          ergonomically by default
graal.G1RSetSparseRegionEntries = 0                                         [Long]
          Max number of entries per region in a sparse table. Will be set
          ergonomically by default.
graal.G1RSetUpdatingPauseTimePercent = 10                                [Integer]
          A target percentage of time that is allowed to be spend on process RS
          update buffers during the collection pause.
graal.G1RefProcDrainInterval = 1000                                      [Integer]
          The number of discovered reference objects to process before draining
          concurrent marking work queues.
graal.G1ReservePercent = 10                                              [Integer]
          It determines the minimum reserve we should have in the heap to
          minimize the probability of promotion failure.
graal.G1SATBBufferEnqueueingThresholdPercent = 60                        [Integer]
          Before enqueueing them, each mutator thread tries to do some filtering
          on the SATB buffers it generates. If post-filtering the percentage of
          retained entries is over this threshold the buffer will be enqueued for
          processing. A value of 0 specifies that mutator threads should not do
          such filtering.
graal.G1SATBBufferSize = 1024                                               [Long]
          Number of entries in an SATB log buffer.
graal.G1UpdateBufferSize = 256                                              [Long]
          Size of an update buffer.
graal.G1UseAdaptiveConcRefinement = true                                 [Boolean]
          Select green, yellow and red zones adaptively to meet the the pause
          requirements.
graal.G1UseAdaptiveIHOP = true                                           [Boolean]
          Adaptively adjust the initiating heap occupancy from the initial value
          of InitiatingHeapOccupancyPercent. The policy attempts to start marking
          in time based on application behavior.
graal.G1VerifyHeapRegionCodeRoots = false                                [Boolean]
          Verify the code root lists attached to each heap region.
graal.G1VerifyRSetsDuringFullGC = false                                  [Boolean]
          If true, perform verification of each heap region's remembered set when
          verifying the heap during a full GC.
graal.GCDebugStartCycle = -1                                             [Integer]
          Start tracing compiled GC barriers after N garbage collections
          (disabled if N <= 0).
graal.GCDrainStackTargetSize = 64                                           [Long]
          Number of entries we will try to leave on the stack during parallel gc
graal.GCPauseIntervalMillis = 201                                           [Long]
          Time slice for MMU specification
graal.GCTimeRatio = 12                                                      [Long]
          Adaptive size policy application time to GC time ratio
graal.GenLoopSafepoints = true                                           [Boolean]
graal.GenerateRuntimeDebugInfo = false                                   [Boolean]
          Generate debuginfo for runtime-compiled code.
graal.GenericDynamicCounters = false                                     [Boolean]
          Turn on the benchmark counters, and displays the results on VM shutdown
graal.GraalArithmeticStubs = true                                        [Boolean]
          Use Graal arithmetic stubs instead of HotSpot stubs where possible
graal.GraalCompileOnly = null                                             [String]
          A filter applied to a method the VM has selected for compilation by
          Graal. A method not matching the filter is redirected to a lower tier
          compiler. The filter format is the same as for the MethodFilter option.
graal.GraphCompressionThreshold = 70                                     [Integer]
          Graal graph compression is performed when percent of live nodes falls
          below this value
graal.GuardHoistingLoopDuplication = true                                [Boolean]
          Duplicate certain loops and eliminate their guards
graal.GuardHoistingLoopDuplicationMaxSize = 64                           [Integer]
          Duplicate only loops up to this estimated size
graal.GuardHoistingLoopDuplicationMinFrequency = 32                      [Integer]
          Duplicate only loops with at least this frequency
graal.GuardHoistingLoopDuplicationMinHotness = 1                            [Long]
          Duplicate only loops in methods executed at least this number of times
graal.GuardPriorities = true                                             [Boolean]
graal.HeapSizePerGCThread = 44040192                                        [Long]
          Size of heap (bytes) per GC thread used in calculating the number of GC
          threads
graal.HeapVerifierVerbosity = 0                                          [Integer]
          Control heap verifier verbosity level: 0 - quiet, 1 - info, 2 -
          warning, 3 - all.
graal.HighTierInversion = false                                          [Boolean]
graal.HighTierPartialUnrolling = true                                    [Boolean]
          Enable EE partial unrolling in high tier.
graal.HotCompilationUnit = false                                         [Boolean]
          Indicates whether a compilation unit is frequently invoked.
graal.HotSpotDeoptExplicitExceptions = false                             [Boolean]
          Testing only option that forces deopts for exception throws
graal.HotSpotPostOnExceptions = false                                    [Boolean]
          Testing only option that forces deopts for exception throws
graal.HotSpotPrintInlining = false                                       [Boolean]
          Print inlining optimizations
graal.HottestPercentageThreshold = 0.125                                  [Double]
          The minimal percentage of the time spent in the method invoked from the
          specific calling-context compared to the total time spent.
graal.HybridStaticContext = false                                        [Boolean]
          Enable hybrid context for static methods, i.e. uses invocation site as
          context for static methods.
graal.IgnoreBadDuplications = true                                       [Boolean]
          Ignore duplications with a bad benefit cost relation.
graal.IgnoreDeoptUsages = true                                           [Boolean]
graal.ImageBuildStatisticsFile = null                                     [String]
          File for printing image build statistics
graal.ImageObjectTreeExpandRoots = ""                                     [String]
          Override the default suppression of specified roots. See: Reports.md.
graal.ImageObjectTreeExpandTypes = ""                                     [String]
          Override the default suppression of specified types. See: Reports.md.
graal.ImageObjectTreeSuppressRoots = ""                                   [String]
          Suppress the expansion of specified roots. See: Reports.md.
graal.ImageObjectTreeSuppressTypes = ""                                   [String]
          Suppress the expansion of specified types. See: Reports.md.
graal.InfeasiblePathCorrelation = true                                   [Boolean]
graal.InfeasiblePathCorrelationWindowSize = 10                           [Integer]
          Limit of the number of dominating if nodes to consider in infeasible
          path correlation to avoid compile time explosion.
graal.InitialHeapSize = 0                                                   [Long]
          Initial heap size (in bytes); zero means use ergonomics
graal.InitialRAMPercentage = 1.5625                                       [Double]
          Percentage of real memory used for initial heap size
graal.InitiatingHeapOccupancyPercent = 45                                [Integer]
          The percent occupancy (IHOP) of the current old generation capacity
          above which a concurrent mark cycle will be initiated. Its value may
          change over time if adaptive IHOP is enabled, otherwise the value
          remains constant. In the latter case a value of 0 will result as
          frequent as possible concurrent marking cycles. A value of 100 disables
          concurrent marking. Fragmentation waste in the old generation is not
          considered free space in this calculation.
graal.Inline = true                                                      [Boolean]
          Enable inlining
graal.InlineAllBonus = 1.0                                                [Double]
          The bonus applied to call nodes that can be fully inlined.
graal.InlineBeforeAnalysis = true                                        [Boolean]
          Inline methods before static analysis
graal.InlineDuringParsing = true                                         [Boolean]
          Inlines trivial methods during bytecode parsing.
graal.InlineDuringParsingMaxDepth = 10                                   [Integer]
          Maximum depth when inlining during bytecode parsing.
graal.InlineEverything = false                                           [Boolean]
graal.InlineMegamorphicCalls = true                                      [Boolean]
          Inline calls with megamorphic type profile (i.e., not all types could
          be recorded).
graal.InlineMonomorphicCalls = true                                      [Boolean]
          Inline calls with monomorphic type profile.
graal.InlinePartialIntrinsicExitDuringParsing = true                     [Boolean]
          Inlines partial intrinsic exits during bytecode parsing when possible.
          A partial intrinsic exit is a call within an intrinsic to the method
          being intrinsified and denotes semantics of the original method that
          the intrinsic does not support.
graal.InlinePolymorphicCalls = true                                      [Boolean]
          Inline calls with polymorphic type profile.
graal.InlineVTableStubs = true                                           [Boolean]
graal.InlinedCompilerNodeLimit = 20000                                   [Integer]
          Controls the maximum number of compiler nodes that can be inlined into
          the compiled method.
graal.InliningCoefficient = 0.02                                          [Double]
          The coefficient used to compute the inlining threshold; the higher, the
          more to inline.
graal.InliningDepthError = 1000                                          [Integer]
          Maximum inlining depth during partial evaluation before reporting an
          infinite recursion
graal.InsertPreMainPostOnly = false                                      [Boolean]
          Do not unroll the main loop, only create pre-main-post.
graal.InspectGraphs = false                                              [Boolean]
          Inspect analysis graphs.
graal.InspectServerContentPath = "inspect"                                [String]
          Path to the contents of the Inspect web server.
graal.InstallSegfaultHandler = null                                      [Boolean]
          Install segfault handler that prints register contents and full Java
          stacktrace. Default: enabled for an executable, disabled for a shared
          library.
graal.InterceptBailout = false                                           [Boolean]
          Intercept also bailout exceptions
graal.Intrinsify = true                                                  [Boolean]
          Use compiler intrinsifications.
graal.InvertMultiEndLoops = false                                        [Boolean]
graal.InvertNonLeafLoops = false                                         [Boolean]
graal.InvertVectorizableLoops = false                                    [Boolean]
graal.IsolatedLoopHeaderAlignment = 32                                   [Integer]
          Alignment in bytes for loop header blocks that have no fall through
          paths.
graal.IterativePeelingLimit = 2                                          [Integer]
          Allow iterative peeling of loops up to this many times (each time the
          peeling phase runs).
graal.IterativePeelingOuterFrequencyBonusThreshold = 4.0                  [Double]
          Allow iterative peeling of loops with an outer frequency bonus above
          this value.
graal.LIRDynMoveProfileMethod = false                                    [Boolean]
          Enable dynamic move profiling per method.
graal.LIROptConstantLoadOptimization = true                              [Boolean]
          Enable constant load optimization.
graal.LIROptControlFlowOptimizer = true                                  [Boolean]
graal.LIROptEdgeMoveOptimizer = true                                     [Boolean]
graal.LIROptLSRAEliminateSpillMoves = true                               [Boolean]
          Enable spill move elimination.
graal.LIROptLSRAOptimizeSpillPosition = true                             [Boolean]
          Enable spill position optimization
graal.LIROptLSStackSlotAllocator = true                                  [Boolean]
          Use linear scan stack slot allocation.
graal.LIROptNullCheckOptimizer = true                                    [Boolean]
graal.LIROptRedundantMoveElimination = true                              [Boolean]
graal.LIROptStackMoveOptimizer = true                                    [Boolean]
graal.LIROptimization = true                                             [Boolean]
          Enable LIR level optimizations.
graal.LIRProfileMethods = false                                          [Boolean]
          Enables profiling of methods.
graal.LIRProfileMoves = false                                            [Boolean]
          Enables profiling of move types on LIR level. Move types are for
          example stores (register to stack), constant loads (constant to
          register) or copies (register to register).
graal.LSRAOptSplitOnly = false                                           [Boolean]
          LSRA optimization: Only split but do not reassign
graal.LSRAOptimization = false                                           [Boolean]
          Enable LSRA optimization
graal.LargeChildrenCountPenaltyCoefficient = 0.005                        [Double]
          Reduces the likelihood of exploring call graphs that have a lot of
          children below the root.
graal.LibGraalManagementDelay = -1                                       [Integer]
          Milliseconds to delay initialization of the libgraal JMX interface.
          Specify a negative value to disable the interface altogether.
graal.LimitInlinedInvokes = 5.0                                           [Double]
graal.LimitObjectArrayLength = false                                     [Boolean]
          Enable a limit for the number of objects recorded for each type of a
          type state before disabling heap sensitivity for that type. The
          analysis must be heap sensitive.
graal.ListMetrics = false                                                [Boolean]
          Lists on the console at VM shutdown the metric names available to the
          Timers, Counters and MemUseTrackers options. Note that this only lists
          the metrics that were initialized during the VM execution and so will
          not include metrics for compiler code that is not executed.
graal.LoadExceptionObjectInVM = false                                    [Boolean]
          Use a VM runtime call to load and clear the exception object from the
          thread at the start of a compiled exception handler.
graal.Log = null                                                          [String]
          Pattern for specifying scopes in which logging is enabled. See the Dump
          option for the pattern syntax.
graal.LogFile = null                                                      [String]
          File to which logging is sent. A %p in the name will be replaced with a
          string identifying the process, usually the process id and %t will be
          replaced by System.currentTimeMillis(). If the current runtime is in an
          isolate, then %i will be replaced by '<isolate id>' otherwise %i is
          removed. An %I is the same as %i except that the replacement is
          '<isolate id>@<isolate address>'. Using %o as filename sends logging to
          System.out whereas %e sends logging to System.err.
graal.LogVerbose = false                                                 [Boolean]
          Enable more verbose log output when available
graal.LoopBoundOptimizationPhase = true                                  [Boolean]
          Try to improve counted loop detection by finding more precise loop
          bounds.
graal.LoopExitVsLoopEndFrequencyDiff = 1000.0                             [Double]
          Scaling factor of frequency difference computed based on loop ends or
          exits
graal.LoopHeaderAlignment = 16                                           [Integer]
          Alignment in bytes for loop header blocks.
graal.LoopInversion = true                                               [Boolean]
graal.LoopMaxUnswitch = 3                                                [Integer]
graal.LoopOnFatalError = false                                           [Boolean]
          Execute an endless loop before printing diagnostics for a fatal error.
graal.LoopPeeling = true                                                 [Boolean]
graal.LoopPredication = true                                             [Boolean]
          Hoists array bounds checks out of simple loops. This is ignored if
          SpeculativeGuardMovement is enabled.
graal.LoopPredicationMainPath = true                                     [Boolean]
          Restricts LoopPredication to only focus on array bounds checks that
          dominate the back edge of a loop.
graal.LoopRotation = true                                                [Boolean]
          Enable Loop Rotation to let the compiler detect more loops as counted.
graal.LoopRotationAssertCountedAfter = false                             [Boolean]
graal.LoopRotationToxicNodeSetMaxNodecost = 512                          [Integer]
          Maximum size in NodeSize of the code to be duplicated during rotation.
graal.LoopUnswitch = true                                                [Boolean]
graal.LoopUnswitchFrequencyBoost = 10.0                                   [Double]
          Number of nodes allowed for a loop unswitching per loop frequency. The
          number of nodes allowed for the unswitching is proportional to the
          relative frequency of the loop by this constant.
graal.LoopUnswitchFrequencyMaxFactor = 0.95                               [Double]
          Maximun value for the frequency factor of an invariant.
graal.LoopUnswitchFrequencyMinFactor = 0.05                               [Double]
          Minimum value for the frequency factor of an invariant.
graal.LoopUnswitchMaxIncrease = 2000                                     [Integer]
          Maximum loop unswitching code size increase in nodes.
graal.LoopUnswitchMinSplitFrequency = 1.0                                 [Double]
          Lower bound for the minimun frequency of an invariant condition to be
          unswitched.
graal.LoopUnswitchTrivial = 10                                           [Integer]
          Number of nodes allowed for a loop unswitching regardless of the loop
          frequency.
graal.MarkStackSize = 4194304                                               [Long]
          Size of marking stack
graal.MarkStackSizeMax = 536870912                                          [Long]
          Maximum size of marking stack
graal.MatchExpressions = true                                            [Boolean]
          Allow backend to match complex expressions.
graal.MaxCallingContextDepth = 0                                         [Integer]
          The maximum length of the methods context chains.
graal.MaxCallingContextWidth = 0                                         [Integer]
          The maximum number of contexts to record for a method. It only affects
          the analysis when the max and min calling context depth are different.
graal.MaxCompilationProblemsPerAction = 2                                [Integer]
          The maximum number of compilation failures to handle with the action
          specified by CompilationFailureAction before changing to a less verbose
          action. This does not apply to the ExitVM action.
graal.MaxConstantObjectsPerType = 100                                    [Integer]
          The maximum number of constant objects recorded for each type before
          merging the constants into one unique constant object per type. The
          analysis must be heap sensitive. It has a minimum value of 1.
graal.MaxCpuLocalsPerCounter = 64                                        [Integer]
          Upper bound on the number of cpu locals per counter. It has to be a
          power of 2.
graal.MaxDirectMemorySize = 0                                               [Long]
          Maximum total size of NIO direct-buffer allocations
graal.MaxDuplicationFactor = 2.0                                          [Double]
          Max amount of extra effort to expend handling irreducible loops. A
          value <= 1 disables support for irreducible loops.
graal.MaxGCPauseMillis = 200                                                [Long]
          Adaptive size policy maximum GC pause time goal in millisecond, or the
          maximum GC time per MMU time slice
graal.MaxGraphSizeNodeCost = 100000                                      [Integer]
          Maximum node cost graph size for duplication. If a graph is bigger
          duplication will stop.
graal.MaxHeapContextDepth = 0                                            [Integer]
          The maximum length of the context used to model a heap object in
          addition to the allocation site; used only when ContextSensitiveHeap is
          enabled.
graal.MaxHeapContextWidth = 0                                            [Integer]
          The maximum number of contexts to record for a heap object. It only
          affects the analysis when the max and min calling context depth are
          different.
graal.MaxHeapFree = 0                                                       [Long]
          The maximum free bytes reserved for allocations, in bytes (0 for
          automatic according to GC policy).
graal.MaxHeapSize = 0                                                       [Long]
          The maximum heap size at run-time, in bytes.
graal.MaxJavaStackTraceDepth = 1024                                      [Integer]
          The maximum number of lines in the stack trace for Java exceptions (0
          means all)
graal.MaxMispredictionCostIncreaseFactor = 2.0                            [Double]
          Abstract measure of the cost of branch misprediction. Higher values
          make generation of conditional moves more likely.
graal.MaxNewSize = 0                                                        [Long]
          The maximum size of the young generation at run-time, in bytes
graal.MaxObjectSetSize = 100                                             [Integer]
          The maximum number of objects recorded for each type of a type state
          before disabling heap sensitivity for that type. The analysis must be
          heap sensitive. It has a minimum value of 1.
graal.MaxPolymorphicDispatches = 3                                       [Integer]
          The maximum number of dispatches in guarded polymorphic inlining.
graal.MaxPriorityInliningPeelingIterations = 10                          [Integer]
          Max number of precise inlining peeling iterations.
graal.MaxRAM = 137438953472                                                 [Long]
          Real memory size (in bytes) used to set maximum heap size
graal.MaxRAMPercentage = 25.0                                             [Double]
          Maximum percentage of real memory used for maximum heap size
graal.MaxSimulationIterations = 2                                        [Integer]
          Maximum simulation-duplication iterations of the duplication
          optimization per invocation.
graal.MaxSplitsPerNode = 32                                              [Integer]
graal.MaxTemplatesPerSnippet = 50                                        [Integer]
graal.MaxTenuringThreshold = 15                                             [Long]
          Maximum value for tenuring threshold
graal.MaxVectorAlignmentUnroll = 4                                       [Integer]
          Maximum number of unrolled alignment instructions
graal.MaxVectorUnroll = 16                                               [Integer]
          Maximum length of linear-code vector operations
graal.MaximumDesiredSize = 20000                                         [Integer]
          Maximum desired size of the compiler graph in nodes.
graal.MaximumEscapeAnalysisArrayLength = 128                             [Integer]
          The maximum length of an array that will be escape analyzed.
graal.MaximumHeapSizePercent = 80                                        [Integer]
          The maximum heap size as percent of physical memory
graal.MaximumInliningSize = 300                                          [Integer]
          Inlining is explored up to this number of nodes in the graph for each
          call site.
graal.MaximumLoopExplosionCount = 10000                                  [Integer]
          Max number of loop explosions per method.
graal.MaximumRecursiveInlining = 5                                       [Integer]
          Maximum level of recursive inlining.
graal.MaximumTransitiveEnabledPullFactor = 2                             [Integer]
          PullThroughPhiOptimization: Maximum number of algorithm iterations per
          optimization invocation.
graal.MaximumYoungGenerationSizePercent = 10                             [Integer]
          The maximum size of the young generation as a percentage of the maximum
          heap size
graal.MegamorphicInliningMinMethodProbability = 0.33                      [Double]
          Minimum probability for methods to be inlined for megamorphic type
          profiles.
graal.MemUseTrackers = null                                               [String]
          Comma separated names of memory usage trackers that are enabled
          irrespective of the value for TrackMemUse option. An empty value
          enables all memory usage trackers unconditionally.
graal.MethodFilter = null                                                 [String]
          Pattern for matching methods. The syntax for a pattern is:

            SourcePatterns = SourcePattern ["," SourcePatterns] .
            SourcePattern = [ "~" ] [ Class "." ] method [ "(" [ Parameter { ";" Parameter } ] ")" ] .
            Parameter = Class | "int" | "long" | "float" | "double" | "short" | "char" | "boolean" .
            Class = { package "." } class .

          Glob pattern matching (*, ?) is allowed in all parts of the source pattern.
          The "~" prefix negates the pattern.

          Positive patterns are joined by an "or" operator: "A,B" matches anything
          matched by "A" or "B". Negative patterns are joined by "and not": "~A,~B"
          matches anything not matched by "A" and not matched by "B". "A,~B,~C,D"
          matches anything matched by "A" or "D" and not matched by "B" and not
          matched by "C".

          A set of patterns containing negative patterns but no positive ones contains
          an implicit positive "*" pattern: "~A,~B" is equivalent to "*,~A,~B".

          Examples of method filters:
          ---------
            *

            Matches all methods in all classes.
          ---------
            canonical(CanonicalizerTool;LogicNode;LogicNode)

            Matches all methods named "canonical", with the first parameter of type
            "CanonicalizerTool", and the second and third parameters of type
            "LogicNode".
            The packages of the parameter types are irrelevant.
          ---------
            arraycopy(Object;;;;)

            Matches all methods named "arraycopy", with the first parameter
            of type "Object", and four more parameters of any type. The
            packages of the parameter types are irrelevant.
          ---------
            List.set

            Matches all methods named "set" in a class whose simple name is "List".
          ---------
            *List.set

            Matches all methods named "set" in a class whose simple name ends with "List".
          ---------
            org.graalvm.compiler.nodes.PhiNode.*

            Matches all methods in the class "org.graalvm.compiler.nodes.PhiNode".
          ---------
            org.graalvm.compiler.nodes.*.canonical

            Matches all methods named "canonical" in classes in the package
            "org.graalvm.compiler.nodes".
          ---------
            arraycopy,toString

            Matches all methods named "arraycopy" or "toString", meaning that ',' acts
            as an "or" operator.
          ---------
            java.util.*.*.,~java.util.*Array*.*
            java.util.*.*.,~*Array*.*

            These patterns are equivalent and match all methods in the package
            "java.util" except for classes that have "Array" in their name.
          ---------
            ~java.util.*.*

            Matches all methods in all classes in all packages except for anything in
            the "java.util" package.
graal.MethodFilterRootOnly = false                                       [Boolean]
          Only check MethodFilter against the root method in the context if true,
          otherwise check all methods
graal.MethodInlineBailoutLimit = 5000                                    [Integer]
          Per-compilation method inlining exploration limit before giving up (use
          0 to disable)
graal.MetricsFile = null                                                  [String]
          File to which metrics are dumped per compilation.
          A CSV format is used if the file ends with .csv otherwise a more
          human readable format is used. The fields in the CSV format are:
                     compilable - method being compiled
            compilable_identity - identity hash code of compilable
                 compilation_nr - where this compilation lies in the ordered
                                  sequence of all compilations identified by
                                  compilable_identity
                 compilation_id - runtime issued identifier for the compilation
                    metric_name - name of metric
                   metric_value - value of metric
graal.MidTierInversion = true                                            [Boolean]
graal.MidTierPartialUnrolling = true                                     [Boolean]
          Enable EE partial unrolling in mid tier.
graal.MinBlockFrequencyPull = 0.66                                        [Double]
          PullThroughPhiOptimization: Ignore low frequency branches during
          duplication.
graal.MinCallingContextDepth = 0                                         [Integer]
          The minimum length of the methods context chains.
graal.MinHeapContextDepth = 0                                            [Integer]
          The minimum length of the context used to model a heap object in
          addition to the allocation site; used only when ContextSensitiveHeap is
          enabled.
graal.MinHeapDeltaBytes = 172032                                            [Long]
          The minimum change in heap space due to GC (in bytes).
graal.MinHeapFreeRatio = 40                                                 [Long]
          The minimum percentage of heap free after GC to avoid expansion.
graal.MinHeapSize = 0                                                       [Long]
          The minimum heap size at run-time, in bytes.
graal.MinPolymorphicDispatchProbability = 0.1                             [Double]
          The minimum probability for using a dispatch in guarded polymorphic
          inlining.
graal.MinRAMPercentage = 50.0                                             [Double]
          Minimum percentage of real memory used for maximum heap size on systems
          with small physical memory size
graal.MinTLABSize = 2048                                                    [Long]
          Minimum allowed TLAB size (in bytes)
graal.MinifyInvertedPhis = true                                          [Boolean]
          Break chained phis
graal.MinimalBulkZeroingSize = 2048                                      [Integer]
          If applicable, use bulk zeroing instructions when the zeroing size in
          bytes exceeds this threshold.
graal.MinimalGraphNodeSizeCheckSize = 1000                               [Integer]
          Minimal size in NodeSize to check the graph size increases of phases.
graal.MinimalRegions = true                                              [Boolean]
          Try to reduce duplication code size to the minimal amount of code.
graal.MinimumBlindedConstantSize = 4                                     [Integer]
          Minimum size (in bytes) of constants to blind.
graal.MinimumPeelFrequency = 0.35                                          [Float]
graal.MoveGuardsUpwards = true                                           [Boolean]
          Move guard nodes to earlier places in the dominator tree if all
          successors of basic block share a common guard condition.
graal.MultiExitCostFactor = 32                                           [Integer]
          Cost/Benefit heuristic for EE unrolling: If a loop has multiple exits,
          cost is increased by this value for every none-sinking loop exit.
graal.MultiExitCostFactorSink = 2                                        [Integer]
          Cost/Benefit heuristic for EE unrolling: If a loop has multiple exits,
          cost is increased by this value for every sinking loop exit.
graal.NDCV = 0                                                           [Integer]
          Run level for NoDeadCodeVerifyHandler (0 = off, 1 = info, 2 = verbose,
          3 = fatal)
graal.NewRatio = 2                                                          [Long]
          Ratio of old/new generation sizes
graal.NewSize = 1048576                                                     [Long]
          Initial new generation size (in bytes)
graal.NodeCounters = false                                               [Boolean]
          Counts the number of instances of each node class.
graal.NonCountedStripMinedBenefitBoost = 64                              [Integer]
          Benefit boost for strip mined non counted loops.
graal.NonCountedStripMiningForceStripAll = false                         [Boolean]
          Force non-counted strip mining for all loops (also counted ones), test
          flag only.
graal.NonCountedStripMiningIgnoreSmallLoops = true                       [Boolean]
          Ignore small loops from strip mining, the iv overhead can cause
          slowdowns.
graal.NonCountedStripMiningInnerLoopTrips = -1                           [Integer]
          The max number of iterations the counted inner loop takes. If -1, the
          frequency of the loop will be used to derive an inner frequency.
graal.NonCountedStripMiningMaximumInnerLoopTrips = 8192                  [Integer]
          If NonCountedStripMiningInnerLoopTrips == -1: Maximum loop trips for
          strip mined non-counted loops.
graal.NonCountedStripMiningMinFrequency = 16.0                            [Double]
          Minimal loop frequency to consider a non-counted loop for strip mining.
graal.NonCountedStripMiningMinimumInnerLoopTrips = 512                   [Integer]
          If NonCountedStripMiningInnerLoopTrips == -1: Minimum loop trips for
          strip mined non-counted loops.
graal.NonCountedStripMiningReuseIVs = true                               [Boolean]
          Try to reuse pre-existing induction variables inside non-counted loops
          for the strip-mined loop's exit check.
graal.NonFatalIdenticalCompilationSnapshots = 20                         [Integer]
          Number of contiguous identical compiler thread stack traces allowed
          before the VM exits on the basis of a stuck compilation.
graal.ObjdumpExecutables = null                                           [String]
          Comma separated list of candidate GNU objdump executables. If not
          specified, disassembling via GNU objdump is disabled. Otherwise, the
          first existing executable in the list is used.
graal.OldPLABSize = 1024                                                    [Long]
          Size of old gen promotion LAB's (in HeapWords)
graal.OldSize = 5242880                                                     [Long]
          Initial tenured generation size (in bytes)
graal.OmitHotExceptionStacktrace = false                                 [Boolean]
graal.OnShutdownCallback = null                                           [String]
          The fully qualified name of a no-arg, void, static method to be invoked
          in HotSpot from libgraal when the libgraal isolate is being
          shutdown.This option exists for the purpose of testing callbacks in
          this context.
graal.OptAssumptions = true                                              [Boolean]
graal.OptBulkAllocation = true                                           [Boolean]
graal.OptCompressedFrameStateValues = true                               [Boolean]
graal.OptConditionalMoves = true                                         [Boolean]
          Optimize simple if branches with conditional moves
graal.OptConvertDeoptsToGuards = true                                    [Boolean]
graal.OptDeDuplication = true                                            [Boolean]
graal.OptDeoptimizationGrouping = true                                   [Boolean]
graal.OptDevirtualizeInvokesOptimistically = true                        [Boolean]
graal.OptDuplication = true                                              [Boolean]
graal.OptEarlyReadElimination = true                                     [Boolean]
graal.OptEliminateGuards = true                                          [Boolean]
graal.OptExactArithmetic = true                                          [Boolean]
graal.OptFastMonitorExit = true                                          [Boolean]
          Straighten monitor enter/exit paths through duplication
graal.OptFloatingReads = true                                            [Boolean]
graal.OptGuardRangeGrouping = true                                       [Boolean]
graal.OptImplicitNullChecks = true                                       [Boolean]
graal.OptLateDuplication = false                                         [Boolean]
graal.OptLockElimination = true                                          [Boolean]
graal.OptLoopPhiStamps = true                                            [Boolean]
          Inject stamps on induction variables.
graal.OptPropagateEquality = true                                        [Boolean]
          Propagate equality into dominated nodes.
graal.OptPullThroughPhi = true                                           [Boolean]
graal.OptReadElimination = true                                          [Boolean]
graal.OptScheduleOutOfLoops = true                                       [Boolean]
graal.OptStringConcat = true                                             [Boolean]
          Optimize StringBuilder construction
graal.OptStringConcatDump = false                                        [Boolean]
          Dump graphs to help debug operation
graal.OptStringConcatDumpUnhandled = false                               [Boolean]
          Dump graphs to help debug operation
graal.OptWriteBarrierElimination = true                                  [Boolean]
          Eliminate redundant write barriers.
graal.OptWriteMotion = false                                             [Boolean]
          Perform write sinking.
graal.OptimisticAliasingAnalysis = true                                  [Boolean]
graal.OptimizeLoopAccesses = true                                        [Boolean]
          Enable access node optimizations for loops
graal.PLABWeight = 75                                                    [Integer]
          Percentage (0-100) used to weight the current sample when computing
          exponentially decaying average for ResizePLAB
graal.ParGCArrayScanChunk = 50                                           [Integer]
          Scan a subset of object array and push remainder, if array is bigger
          than this
graal.ParallelGCBufferWastePct = 10                                      [Integer]
          Wasted fraction of parallel allocation buffer
graal.ParallelGCThreads = 0                                              [Integer]
          Number of parallel threads parallel gc will use
graal.ParallelRefProcBalancingEnabled = true                             [Boolean]
          Enable balancing of reference processing queues
graal.ParallelRefProcEnabled = false                                     [Boolean]
          Enable parallel reference processing whenever possible
graal.PartialEscapeAnalysis = true                                       [Boolean]
graal.PartialRedundancyElimination = true                                [Boolean]
          Enable partial redundancy elimination
graal.PartialUnroll = true                                               [Boolean]
graal.PartialUnrollCostReductionFactorHighTier = 2                       [Integer]
          Cost/Benefit heuristic for EE unrolling in high tier: reduce cost by a
          constant factor when comparing with relative benefit.
graal.PartialUnrollCostReductionFactorMidTier = 8                        [Integer]
          Cost/Benefit heuristic for EE unrolling in mid tier: reduce cost by a
          constant factor when comparing with relative benefit.
graal.PartialUnrollMaxIterationsHighTier = 4                             [Integer]
          Maximum number of iterations to unroll for a high tier main loop.
graal.PartialUnrollMaxIterationsMidTier = 16                             [Integer]
          Maximum number of iterations to unroll for a mid tier main loop.
graal.PartialUnrollMaxSizeHighTier = 256                                 [Integer]
          Maximum node cost size of a loop to be considered for high tier
          unrolling.
graal.PartialUnrollMaxSizeMidTier = 256                                  [Integer]
          Maximum node cost size of a loop to be considered for mid tier tier
          unrolling.
graal.PartialUnrollMinFrequency = 4                                      [Integer]
          Minimal loop frequency to consider a loop for partial unrolling
graal.PathProfileCutThreshold = 10                                       [Integer]
          The limit on the number of paths at control-flow merges. Decreasing
          this value reduces the number of paths, but also shortens them.
graal.PathProfileDumpFile = null                                          [String]
          Dump information for path profile (null or file name). If set to null,
          then dumping is disabled.
graal.PathProfileFrequentThreshold = 500                                    [Long]
          Maximum acceptable number of paths coming from the inbound of a merge
          if both of them are frequent.
graal.PathProfileGlobalLowFrequencyRatio = 0.1                            [Double]
          If some block's relative frequency drops below this number times the
          maximum relative frequency in the graph, then the block is considered
          infrequent.
graal.PathProfileLocalLowFrequencyRatio = 10.0                            [Double]
          If the ratio of the merge's frequency with its inbound's frequency is
          greater than this threshold, then the inbound is considered infrequent.
graal.PathProfileMaxTotalCounters = 4000000                              [Integer]
          Maximum number of counters to use in path profiling for all
          instrumented methods.
graal.PathProfilePolicy = None                                            [String]
          Enable or disable the path-profiling algorithm. If it enables it, it
          also allows to select which mode to execute.
graal.PathProfileRegenerate = false                                      [Boolean]
          Controls whether the path-regeneration algorithm is executed.
graal.PeelALot = false                                                   [Boolean]
graal.PeelFoldFactor = 120                                               [Integer]
graal.PeelingConsideredMinLoopIterations = 1.5                            [Double]
          Minimal loop body iterations necessary to consider peeling.
graal.PeelingConsideredMinRelativeFrequency = 4.0                         [Double]
          Minimal relative frequency of loop begin necessary to consider peeling.
graal.PeelingHighTierCostReductionFactor = 64.0                           [Double]
          Cost/Benefit heuristic for EE simulation-based loop peeling in high
          tier: reduce cost by a constant factor when comparing with relative
          benefit.
graal.PeelingMidTierCostReductionFactor = 8.0                             [Double]
          Cost/Benefit heuristic for EE simulation-based loop peeling in mid
          tier: reduce cost by a constant factor when comparing with relative
          benefit.
graal.PenalizeComplexLoopControlFlow = true                              [Boolean]
          Increase the cost of duplicating control flow splits inside loops if
          they are not foldable.The generally tend to complicate control flow and
          generate worse code in the backend.
graal.PercentTimeInIncrementalCollection = 50                            [Integer]
          Percentage of total collection time that should be spent on young
          generation collections.
graal.PerfDataMemorySize = 32768                                         [Integer]
          Size of performance data memory region. Will be rounded up to a
          multiple of the native os page size.
graal.PerfDataSamplingInterval = 200                                     [Integer]
          Jvmstat instrumentation sampling interval (in milliseconds)
graal.PerfMaxStringConstLength = 1024                                    [Integer]
          Maximum PerfStringConstant string length before truncation
graal.PhiMinificationMinimalLoopFrequency = 2.0                           [Double]
          Minimal loop frequency to consider a loop for inverted phi minifaction.
graal.PreTouchParallelChunkSize = 1073741824                                [Long]
          Per-thread chunk size for parallel memory pre-touch.
graal.PreferContainerQuotaForCPUCount = true                             [Boolean]
          Calculate the container CPU availability based on the value of quotas
          (if set), when true. Otherwise, use the CPU shares value, provided it
          is less than quota.
graal.PrefetchCopyIntervalInBytes = -1                                      [Long]
          How far ahead to prefetch destination area (<= 0 means off)
graal.PrefetchScanIntervalInBytes = -1                                      [Long]
          How far ahead to prefetch scan area (<= 0 means off)
graal.PrintAnalysisCallTree = false                                      [Boolean]
          Print analysis call tree, a breadth-first tree reduction of the call
          graph.
graal.PrintAnalysisCallTreeType = TXT                                     [String]
          Change the output format of the analysis call tree, available options
          are TXT and CSV. See: Reports.md.
graal.PrintAnalysisStatistics = false                                    [Boolean]
          Print analysis results statistics.
graal.PrintBackendCFG = false                                            [Boolean]
          Enable dumping scheduled HIR, LIR, register allocation and code
          generation info to the C1Visualizer.
graal.PrintBlockMapping = false                                          [Boolean]
          Enable dumping CFG built during initial BciBlockMapping
graal.PrintCallEdges = false                                             [Boolean]
          Print call edges with other analysis results statistics.
graal.PrintCanonicalGraphStringFlavor = 0                                [Integer]
          Choose format used when dumping canonical text for graphs: 0 gives a
          scheduled graph (better for spotting changes involving the schedule)
          while 1 gives a CFG containing expressions rooted at fixed nodes
          (better for spotting small structure differences)
graal.PrintCanonicalGraphStrings = false                                 [Boolean]
          Enable dumping canonical text from for graphs.
graal.PrintCompilation = false                                           [Boolean]
          Print an informational line to the console for each completed
          compilation.
graal.PrintDetailedAllocationProfiling = true                            [Boolean]
          Print detailed information for each allocation site
graal.PrintFlags = null                                                   [String]
          Show available options based on comma-separated option-types (allowed
          categories: User, Expert, Debug).
graal.PrintFlagsWithExtraHelp = null                                      [String]
          Print extra help, if available, based on comma-separated option names.
          Pass * to show all options that contain extra help.
graal.PrintGC = false                                                    [Boolean]
          Print summary GC information after each collection.
graal.PrintGCSummary = false                                             [Boolean]
          Print summary GC information after application main method returns.
graal.PrintGCTimeStamps = false                                          [Boolean]
          Print a time stamp at each collection, if +PrintGC or +VerboseGC.
graal.PrintGCTimes = false                                               [Boolean]
          Print the time for each of the phases of each collection, if
          +VerboseGC.
graal.PrintGraph = File                                                   [String]
          Where IdealGraphVisualizer graph dumps triggered by Dump or DumpOnError
          should be written.
          The accepted values are:
                File - Dump IGV graphs to the local file system (see DumpPath).
             Network - Dump IGV graphs to the network destination specified by PrintGraphHost and PrintGraphPort.
                       If a network connection cannot be opened, dumping falls back to file dumping.
             Disable - Do not dump IGV graphs.
graal.PrintGraphFile = true                                              [Boolean]
          Setting to true sets PrintGraph=file, setting to false sets
          PrintGraph=network
graal.PrintGraphHost = "127.0.0.1"                                        [String]
          Host part of the address to which graphs are dumped.
graal.PrintGraphPort = 4445                                              [Integer]
          Port part of the address to which graphs are dumped in binary format.
graal.PrintGraphWithSchedule = false                                     [Boolean]
          Schedule graphs as they are dumped.
graal.PrintHeapShape = false                                             [Boolean]
          Print the shape of the heap before and after each collection, if
          +VerboseGC.
graal.PrintIRWithLIR = false                                             [Boolean]
          Print HIR along side LIR as the latter is generated
graal.PrintImageObjectTree = false                                       [Boolean]
          Print image object hierarchy.
graal.PrintLIRWithAssembly = false                                       [Boolean]
          Include the LIR as comments with the final assembly.
graal.PrintPointsToStatistics = false                                    [Boolean]
          Report analysis statistics.
graal.PrintProfilingInformation = false                                  [Boolean]
          Print profiling information when parsing a method's bytecode
graal.PrintSynchronizedAnalysis = false                                  [Boolean]
          Print types used for Java synchronization.
graal.PrintUnmodifiedGraphs = true                                       [Boolean]
          Dump a graph even if it has not changed since it was last dumped.
          Change detection is based on adding and deleting nodes or changing
          inputs.
graal.PriorityInliningPolicy = ""                                         [String]
          The policy to use, must be empty for automatic resolution.
graal.PriorityInliningTuningPolicy = "DomainSpecific"                     [String]
          Comma-separated list of analysis policies for exploring the methods in
          the call graph and for inlining, empty for no policy.
graal.ProfileAllocations = false                                         [Boolean]
          Enable profiling of allocation sites.
graal.ProfileAllocationsContext = AllocatingMethod                        [String]
          Control the naming and granularity of the counters when using
          ProfileAllocations.
          The accepted values are:
                  AllocatingMethod - a counter per method
                   InstanceOrArray - one counter for all instance allocations and
                                     one counter for all array allocations
                     AllocatedType - one counter per allocated type
            AllocatedTypesInMethod - one counter per allocated type, per method

graal.ProfileAnalysisOperations = false                                  [Boolean]
          Track the progress of the static analysis.
graal.ProfileCompiledMethods = false                                     [Boolean]
graal.ProfileConstantObjects = false                                     [Boolean]
          Track the creation of constant objects.
graal.ProfileDumpPeriod = -1                                             [Integer]
          Integer greater than zero representing the duration in seconds that
          will be used to trigger a profile capture. Any integer less than one
          disables periodic dumps
graal.ProfileDumpingVerbose = false                                      [Boolean]
          Emit a message to stderr after dumping a profile.
graal.ProfileInferenceMethodFilter = "*"                                  [String]
          Restrict profile inference to methods matching the regex (a list of
          comma separated, optionally negated filter patterns).
graal.ProfileLockElimination = false                                     [Boolean]
graal.ProfileMonitors = false                                            [Boolean]
          Enable profiling of monitor operations.
graal.ProfileOptBulkAllocation = false                                   [Boolean]
graal.ProfileSelfTime = true                                             [Boolean]
          Excludes time spent in invoked methods; measures total time including
          subcalls when turned off.
graal.ProfilesDumpFile = "default.iprof"                                  [String]
          Value should point to a profile dump file.
graal.PropagateEqualityDepth = 6                                         [Integer]
          Maximum depth of dependency when propagating equals property.
graal.PruneLargeDominatorUsageTrees = true                               [Boolean]
graal.PullThroughPhiCodeSizeIncrease = 0.1                                [Double]
          PullThroughPhiOptimization: Percentage in node cost graph size for the
          floating node duplication budget. Computed relative to the method's
          graph size.
graal.QueuedAllocationWarningCount = 0                                      [Long]
          Number of times an allocation that queues behind a GC will retry before
          printing a warning
graal.RawConditionalElimination = true                                   [Boolean]
graal.ReadEliminationMaxLoopVisits = 5                                   [Integer]
graal.ReadProxySchedulingStrategy = LATEST_OUT_OF_LOOPS                   [String]
          Chose the scheduling strategy for inserting the read proxies.
graal.ReassociateExpressions = true                                      [Boolean]
          Re-associate loop invariants and constants.
graal.ReduceDCE = true                                                   [Boolean]
          Disable optional dead code eliminations
graal.RefDiscoveryPolicy = 0                                             [Integer]
          Select type of reference discovery policy: reference-based(0) or
          referent-based(1)
graal.RegisterPressure = null                                             [String]
          Comma separated list of registers that register allocation is limited
          to.
graal.RelativeBenefitInliningCoefficient = 0.001                          [Double]
          The coefficient used to compute the inlining threshold; the higher, the
          hard to inline.
graal.RelaxTypeFlowStateConstraints = true                               [Boolean]
          Allow a type flow state to contain types not compatible with its
          declared type.
graal.RemoveNeverExecutedCode = true                                     [Boolean]
graal.RemoveSaturatedTypeFlows = true                                    [Boolean]
          Enable the type flow saturation analysis performance optimization.
graal.ReplaceInputsWithConstantsBasedOnStamps = true                     [Boolean]
graal.ResizePLAB = true                                                  [Boolean]
          Dynamically resize (survivor space) promotion LAB's
graal.ResizeTLAB = true                                                  [Boolean]
          Dynamically resize TLAB size for threads
graal.RespectVectorization = true                                        [Boolean]
          Try avoid unrolling vectorizable loops.
graal.RewriteStripMinedCounterTo32Bit = true                             [Boolean]
          Rewrite the counter of a strip mined loop to have a 32bit type.
graal.RotateNonLeafLoops = false                                         [Boolean]
graal.RuntimeSourceDestDir = null                                         [String]
          Directory where Java source-files will be placed for the debugger
graal.SIMDVectorizationDirectLoadStore = false                           [Boolean]
          Allow SIMDVectorization to vectorize load to store opportunities when
          there are no matching SIMD operations between load and store
graal.SIMDVectorizationSingletons = false                                [Boolean]
          Enable matching of singleton groups to increase corner-case matching
graal.SIMDVectorizationVolatileLoads = false                             [Boolean]
          Allow load grouping to include grouping of volatile loads. Note
          currently this may generate incorrect results.
graal.SIMDVectorizationVolatileWrites = false                            [Boolean]
          Allow store grouping to include grouping of volatile writes. Note
          currently this may generate incorrect results.
graal.SIMDVectorizationWindowSize = 4                                    [Integer]
          Set the number of dominating and dominated blocks scanned per block
graal.SafepointPromptnessFailureNanos = 0                                   [Long]
          Exit the VM if I can not come to a safepoint in this many nanoseconds.
          0 implies forever.
graal.SafepointPromptnessWarningNanos = 0                                   [Long]
          Print a warning if I can not come to a safepoint in this many
          nanoseconds. 0 implies forever.
graal.SamplingBasedProfiling = false                                     [Boolean]
          Allow sampling-based profiling. Default: disabled in execution.
graal.ScanObjectsParallel = true                                         [Boolean]
          Object scanning in parallel
graal.ScheduledDuplicationSimulation = false                             [Boolean]
          Simulation can either only process fixed nodes or schedule the graph
          and also process floating nodes.
graal.ShowConfiguration = none                                            [String]
          Writes to the VM log information about the compiler configuration
          selected.
graal.ShowDumpFiles = false                                              [Boolean]
          Print the name of each dump file path as it's created.
graal.ShowSubstitutionSourceInfo = false                                 [Boolean]
          Controls whether the source position information of snippets and method
          substitutions are exposed to HotSpot. Can be useful when profiling to
          get more precise position information.
graal.SimpleFastInflatedLocking = true                                   [Boolean]
          Handle simple cases for inflated monitors in the fast-path.
graal.SimulationBasedLoopPeeling = true                                  [Boolean]
          Use DBDS algorithm to simulate the impact of peeling on a loop.
graal.SimulationPruneUnlikelyBranches = true                             [Boolean]
          Ignore low frequency branches during simulation.
graal.SmallCompiledLowLevelGraphSize = 330                               [Integer]
          If the previous low-level graph size of the method exceeds the
          threshold, it is not inlined.
graal.SmallGraphDuplicationBudgetFactor = 1.0                             [Double]
          See 'DuplicationBudgetFactor': for small graphs.
graal.SmallGraphSize = 2000                                              [Integer]
          Node cost graph size for a graph to be considered 'small'.
graal.SmallRootIrPenaltyCoefficient = 0.02                                [Double]
          Reduces the likelihood of exploring call graphs with IR size much
          larger than the root.
graal.SnippetCounters = false                                            [Boolean]
          Enable counters for various paths in snippets.
graal.SoftRefLRUPolicyMSPerMB = 1000                                        [Long]
          Number of milliseconds per MB of free space in the heap.
graal.SpectrePHTBarriers = None                                           [String]
          Select a strategy to mitigate speculative bounds check bypass (aka
          Spectre-PHT or Spectre V1).
          This is an experimental option - execution of untrusted code is not supported by GraalVM CE.
          The accepted values are:
                            None - No mitigations are used in JIT compiled code.
                      AllTargets - Speculative execution on all conditional branch targets is
                                   stopped using speculative execution barrier instructions.
                    GuardTargets - Branch targets relevant to Java memory safety are instrumented
                                   with barrier instructions. This option has less performance impact
                                   than AllTargets.
            NonDeoptGuardTargets - Same as GuardTargets, except that branches which deoptimize are not
                                   protected since they can not be executed repeatedly and are thus less
                                   likely to be successfully exploited in an attack.


          Note that all modes except "None" will also instrument branch target blocks containing UNSAFE memory accesses
          with barrier instructions.
graal.SpectrePHTIndexMasking = false                                     [Boolean]
          Mask indices to scope access to allocation size after bounds check.
graal.SpeculativeGuardMovement = true                                    [Boolean]
          Move loop invariant guards (e.g., array bounds checks) out of loops.
graal.SpeculativeStoreCheck = true                                       [Boolean]
          Speculates that arrays have exact type to optimize store checks
graal.StackSize = 0                                                         [Long]
          The size of each thread stack at run-time, in bytes.
graal.StartFlightRecording = ""                                           [String]
          Start flight recording with options.
graal.StressExplicitExceptionCode = false                                [Boolean]
          Stress the code emitting explicit exception throwing code.
graal.StressInvokeWithExceptionNode = false                              [Boolean]
          Stress the code emitting invokes with explicit exception edges.
graal.StressTestEarlyReads = false                                       [Boolean]
          Stress the code by emitting reads at earliest instead of latest point.
graal.StrictDeoptInsertionChecks = false                                 [Boolean]
          Perform checks that guards and deopts aren't introduced in graphs that
          should handle exceptions explicitly
graal.StringIndexOfConstantLimit = 4096                                  [Integer]
          String.indexOf invocations will be evaluated at compile time if the
          receiver is a constant and its length is smaller than this value.
graal.StripMineALot = false                                              [Boolean]
          Force strip mining of all loops that can be strip mined.
graal.StripMineCountedLoops = false                                      [Boolean]
graal.StripMineInvertedLoops = true                                      [Boolean]
          Strip mine inverted loops.
graal.StripMineNonCountedLoops = true                                    [Boolean]
graal.SupportJsrBytecodes = true                                         [Boolean]
graal.SupportOSRWithLocks = true                                         [Boolean]
          Support OSR compilations with locks. If DeoptAfterOSR is true we can
          per definition not have unbalanced enter/exits mappings. If
          DeoptAfterOSR is false insert artificial monitor enters after the
          OSRStart to have balanced enter/exits in the graph.
graal.SurvivorRatio = 8                                                     [Long]
          Ratio of eden/survivor space size
graal.TLABAllocationWeight = 35                                          [Integer]
          Allocation averaging weight
graal.TLABRefillWasteFraction = 64                                          [Long]
          Maximum TLAB waste at a refill (internal fragmentation)
graal.TLABSize = 0                                                          [Long]
          Starting TLAB size (in bytes); zero means set ergonomically
graal.TLABWasteIncrement = 4                                                [Long]
          Increment allowed waste at slow allocation
graal.TLABWasteTargetPercent = 1                                         [Integer]
          Percentage of Eden that can be wasted
graal.TargetPLABWastePct = 10                                            [Integer]
          Target wasted space in last buffer as percent of overall allocation
graal.TargetSurvivorRatio = 50                                              [Long]
          Desired percentage of survivor space used after scavenge
graal.TearDownFailureNanos = 0                                              [Long]
          The number of nanoseconds before tearing down an isolate gives a
          failure message. 0 implies no message.
graal.TearDownWarningNanos = 0                                              [Long]
          The number of nanoseconds before and between which tearing down an
          isolate gives a warning message. 0 implies no warning.
graal.Time = null                                                         [String]
          Pattern for specifying scopes in which timing is enabled. See the Dump
          option for the pattern syntax. An empty value enables all timers
          unconditionally.
graal.TimeStampProfiling = false                                         [Boolean]
          Profile method execution time.
graal.TimedDynamicCounters = -1                                          [Integer]
          Turn on the benchmark counters, and displays the results every n
          milliseconds
graal.Timers = null                                                       [String]
          Comma separated names of timers that are enabled irrespective of the
          value for Time option. An empty value enables all timers
          unconditionally.
graal.TraceAuxiliaryImageClassHistogram = false                          [Boolean]
          Enables detailed tracing of auxiliary image events.
graal.TraceAuxiliaryImageReferenceTree = false                           [Boolean]
          Enables detailed tracing of auxiliary image events.
graal.TraceBytecodeParserLevel = 0                                       [Integer]
          The trace level for the bytecode parser. A value of 1 enables
          instruction tracing and any greater value emits a frame state trace
          just prior to each instruction trace.Instruction tracing output from
          multiple compiler threads will be interleaved so use of this option
          make most sense for single threaded compilation. The MethodFilter
          option can be used to refine tracing to selected methods.
graal.TraceCodeCache = false                                             [Boolean]
          Print logging information for runtime code cache modifications
graal.TraceDeoptimization = false                                        [Boolean]
          Print logging information for every deoptimization
graal.TraceDeoptimizationDetails = false                                 [Boolean]
          Print verbose logging information for every deoptimization
graal.TraceEscapeAnalysis = false                                        [Boolean]
graal.TraceExceptionHandlerStub = false                                  [Boolean]
          Trace execution of stub used to handle an exception thrown by a callee.
graal.TraceHeapChunks = false                                            [Boolean]
          Trace heap chunks during collections, if +VerboseGC and
          +PrintHeapShape.
graal.TraceInlineDuringParsing = false                                   [Boolean]
          Traces inlining performed during bytecode parsing.
graal.TraceInlining = false                                              [Boolean]
          Enable tracing of inlining decisions.
          Output format:
            compilation of 'Signature of the compilation root method':
              at 'Signature of the root method' ['Bytecode index']: <'Phase'> 'Child method signature': 'Decision made about this callsite'
                at 'Signature of the child method' ['Bytecode index']:
                   |--<'Phase 1'> 'Grandchild method signature': 'First decision made about this callsite'
                   \--<'Phase 2'> 'Grandchild method signature': 'Second decision made about this callsite'
                at 'Signature of the child method' ['Bytecode index']: <'Phase'> 'Another grandchild method signature': 'The only decision made about this callsite.'
graal.TraceInliningForStubsAndSnippets = false                           [Boolean]
          Enable inlining decision tracing in stubs and snippets.
graal.TraceLIRGeneratorLevel = 0                                         [Integer]
          The trace level for the LIR generator
graal.TraceMonitorsMethodFilter = null                                    [String]
          Trace monitor operations in methods whose fully qualified name contains
          this substring.
graal.TraceMonitorsTypeFilter = null                                      [String]
          Trace monitor operations on objects whose type contains this substring.
graal.TraceParserPlugins = false                                         [Boolean]
          Traces use of plugins during bytecode parsing.
graal.TraceUnwindStub = false                                            [Boolean]
          Trace execution of the stub that routes an exception to a handler in
          the calling frame.
graal.TrackAccessChain = false                                           [Boolean]
          Track the callers for methods and accessing methods for fields.
graal.TrackGraphSizesInDuplication = false                               [Boolean]
          Enable (if Count is enabled) graph size tracking during every
          duplication iteration.
graal.TrackInliningStatistics = none                                      [String]
          Track inlining statistics (inlining duration, call tree size, compiler
          node counts, and the number of callsites). One of: none, interactive
graal.TrackInputFlows = false                                            [Boolean]
          Track the input for type flows.
graal.TrackMemUse = null                                                  [String]
          Pattern for specifying scopes in which memory use tracking is enabled.
          See the Dump option for the pattern syntax. An empty value enables all
          memory use trackers unconditionally.
graal.TrackNodeInsertion = false                                         [Boolean]
          Track source stack trace where a node was inserted into the graph.
graal.TrackNodeSourcePosition = false                                    [Boolean]
          Track the NodeSourcePosition.
graal.TrivialInliningSize = 10                                           [Integer]
          Graphs with less than this number of nodes are trivial and therefore
          always inlined.
graal.TrivialLoopSizeLimitForPeeling = 512.0                              [Double]
          Loop peeling will consider any loop with a size (in terms of estimated
          machine instructions) below this value to be a prime candidate for
          peeling. Larger loops will only be considered for peeling if the
          simulated benefit of peeling is relatively high. The larger the loop,
          the greater the expected benefit has to be.
graal.TruffleCompilerConfiguration = null                                 [String]
          Select a compiler configuration for Truffle compilation (default: use
          Graal system compiler configuration).
graal.TruffleHostInlining = true                                         [Boolean]
          Whether Truffle host inlining is enabled.
graal.TruffleHostInliningBaseBudget = 5000                               [Integer]
          Maximum budget for Truffle host inlining for runtime compiled methods.
graal.TruffleHostInliningByteCodeInterpreterBudget = 100000              [Integer]
          Maximum budget for Truffle host inlining for runtime compiled methods
          with a BytecodeInterpreterSwitch annotation.
graal.TruffleHostInliningMaxExplorationDepth = 1000                      [Integer]
          Determines the maximum call depth for exploration during host inlining.
graal.TruffleHostInliningPrintExplored = false                           [Boolean]
          When logging is activated for this phase enables printing of only
          explored, but ultimately not inlined call trees.
graal.TrustFinalDefaultFields = true                                     [Boolean]
          Determines whether to treat final fields with default values as
          constant.
graal.TryExplodeOverPhis = true                                          [Boolean]
          PullThroughPhiOptimization: Enable floating node duplication over
          multiple phi nodes at once.
graal.TryPhiPhiPulls = true                                              [Boolean]
          PullThroughPhiOptimization: Enable floating node duplication over phis
          where the target node has different phis as input.
graal.TuneInlinerExploration = 0.0                                        [Double]
          Increases or decreases the time spent exploring inlining opportunities
          under the assumption that more time results in better peak performance
          and less time reduces time to reach (a lower) peak performance. The
          value of the option is clamped between -1 and 1 inclusive. Anything
          below 0, reduces the exploration time and anything above 0 increases
          exploration time. Note that this option is only a heuristic and should
          be tuned for any specific application.
graal.TypeCheckMaxHints = 2                                              [Integer]
          The maximum number of profiled types that will be used when compiling a
          profiled type check. Note that TypeCheckMinProfileHitProbability also
          influences whether profiling info is used in compiled type checks.
graal.TypeCheckMinProfileHitProbability = 0.5                             [Double]
          If the probability that a type check will hit one the profiled types
          (up to TypeCheckMaxHints) is below this value, the type check will be
          compiled without profiling info
graal.TypeFlowPrinterInRadius = 0                                        [Integer]
          How many levels of inputs to print. A value of 0 prints only the target
          flow.
graal.TypeFlowPrinterOutRadius = 0                                       [Integer]
          How many levels of outputs to print. A value of 0 prints only the
          target flow.
graal.TypeFlowSaturationCutoff = 20                                      [Integer]
          The maximum number of types recorded in a type flow. -1 indicates no
          limitation.
graal.TypicalCallGraphSize = 200                                         [Integer]
          Denotes the call graph size that is considered medium size.
graal.TypicalGraphSize = 3250                                            [Integer]
          The typical graph size at which inlining pressure must start growing.
graal.TypicalGraphSizeInvokeBonus = 70                                   [Integer]
          The increase in estimated typical graph size after inlining, per each
          extra invoke.
graal.TypicalGraphSizeMax = 15000                                        [Integer]
          The maximum in estimated inlined typical graph size.
graal.UnresolvedIsError = true                                           [Boolean]
          Report unresolved elements as errors.
graal.UnrollEmptyLoops = false                                           [Boolean]
          Unroll empty loops.
graal.UnrollInvertedLoops = true                                         [Boolean]
          Unroll inverted (tail counted) loops.
graal.UnrollMaxIterations = 16                                           [Integer]
graal.UnrollMultiEndLoops = true                                         [Boolean]
          Unroll loops with multiple loop ends.
graal.UnrollMultiExitLoops = true                                        [Boolean]
          Unroll loops with multiple loop exits.
graal.UseBranchesWithin32ByteBoundary = false                            [Boolean]
          Force branch instructions to align with 32-bytes boundary, to mitigate
          the jcc erratum. See
          https://www.intel.com/content/dam/support/us/en/documents/processors/mitigations-jump-conditional-code-erratum.pdf
          for more details. If not set explicitly, the default value will be
          determined according to the CPU model.
graal.UseCompilationStatistics = false                                   [Boolean]
          Enables CompilationStatistics.
graal.UseDynamicNumberOfGCThreads = true                                 [Boolean]
          Dynamically choose the number of threads up to a maximum of
          ParallelGCThreads parallel collectors will use for garbage collection
          work
graal.UseExceptionProbability = true                                     [Boolean]
graal.UseGraalStubs = true                                               [Boolean]
          Use Graal-generated stubs for complicated LIR operations instead of
          embedding all the emitted code.
graal.UseGraphCache = true                                               [Boolean]
          Turn on graph caching.
graal.UseLoopEndFrequencies = false                                      [Boolean]
          Derive loop frequencies only from backedge frequencies instead of from
          loop exit frequencies.
graal.UseLoopLimitChecks = true                                          [Boolean]
graal.UsePerfData = true                                                 [Boolean]
          Flag to disable jvmstat instrumentation for performance testing.
graal.UsePriorityInlining = true                                         [Boolean]
          Use priority-based inlining.
graal.UseSnippetGraphCache = true                                        [Boolean]
          Use a cache for snippet graphs.
graal.UseSnippetTemplateCache = true                                     [Boolean]
          Use a LRU cache for snippet templates.
graal.UseTrappingNullChecks = true                                       [Boolean]
          Use traps for null checks instead of explicit null-checks
graal.UseTypeCheckHints = true                                           [Boolean]
graal.VTuneAbsoluteFilenames = true                                      [Boolean]
          Use absolute path for source-filenames in VTune events.
graal.VectorFoldMinIterations = 4                                        [Integer]
          Only generate SIMD loops for vector folds expected to iterate at least
          this many times.
graal.VectorIntrinsics = true                                            [Boolean]
          Enable vectorized array copy intrinsics
graal.VectorPolynomialIntrinsics = false                                 [Boolean]
          Enable vectorized polynomial intrinsics
graal.VectorUnroll = 1                                                   [Integer]
          Unroll vectorized loops
graal.Vectorization = true                                               [Boolean]
          Enable vectorization.
graal.VectorizeAllocation = true                                         [Boolean]
          Enable vectorized array initialization
graal.VectorizeConditional = true                                        [Boolean]
          Enable vectorization of conditional code.
graal.VectorizeDeopts = true                                             [Boolean]
          Enable vectorization of loops with conditional deopts before writes.
graal.VectorizeFoldShaped = true                                         [Boolean]
          Enable vectorization of loops implementing a higher-order 'fold'
          function.
graal.VectorizeGather = true                                             [Boolean]
          Enable vectorization of vector gather operations.
graal.VectorizeHashes = true                                             [Boolean]
          Enable vectorization of hashCode patterns.
graal.VectorizeLoops = true                                              [Boolean]
          Enable vectorization of loops
graal.VectorizeMapShaped = true                                          [Boolean]
          Enable vectorization of loops implementing a higher-order 'map'
          function.
graal.VectorizeNegativeStride = true                                     [Boolean]
          Enable vectorization of loops with negative strides.
graal.VectorizeReachabilityFences = true                                 [Boolean]
          Enable vectorization of loops with reachability fences.
graal.VectorizeSIMD = true                                               [Boolean]
          Enable detection of SIMD patterns
graal.VectorizeSafepoints = true                                         [Boolean]
          Enable vectorization of loops with safepoints.
graal.VectorizeSequence = true                                           [Boolean]
          Enable vectorization of sequence values.
graal.VerboseGC = false                                                  [Boolean]
          Print more information about the heap before and after each collection.
graal.Verify = null                                                       [String]
          Pattern for specifying scopes in which logging is enabled. See the Dump
          option for the pattern syntax.
graal.VerifyAfterGC = false                                              [Boolean]
          Verify memory system after GC
graal.VerifyBalancedMonitors = false                                     [Boolean]
          Emit extra code to dynamically check monitor operations are balanced.
graal.VerifyBeforeGC = false                                             [Boolean]
          Verify memory system before GC
graal.VerifyDuplicationOperations = false                                [Boolean]
graal.VerifyDuringGC = false                                             [Boolean]
          Verify memory system during GC (between phases)
graal.VerifyGCStartAt = 0                                                   [Long]
          GC invoke count where +VerifyHeap kicks in
graal.VerifyGraalGraphEdges = false                                      [Boolean]
          Perform expensive verification of graph inputs, usages, successors and
          predecessors
graal.VerifyGraalGraphs = true                                           [Boolean]
          Verify graphs often during compilation when assertions are turned on
graal.VerifyGraalPhasesSize = false                                      [Boolean]
          Verify before - after relation of the relative, computed, code size of
          a graph
graal.VerifyHeapAtReturn = false                                         [Boolean]
          Perform platform dependent validation of the Java heap at returns
graal.VerifyKillCFGUnusedNodes = false                                   [Boolean]
          Verify that there are no new unused nodes when performing killCFG
graal.VerifyLoopVectorization = false                                    [Boolean]
          Run expensive checks to verify the graph after loop vectorization.
graal.VerifyPhases = false                                               [Boolean]
graal.VerifyRememberedSets = false                                       [Boolean]
          Verify GC remembered sets
graal.VerifyWriteBarrierElimination = false                              [Boolean]
          Add code to verify that eliminated barriers weren't needed.
graal.WarnMissingIntrinsic = false                                       [Boolean]
          Print a warning when a missing intrinsic is seen.
graal.WriteableCodeCache = false                                         [Boolean]
          Allocate code cache with write access, allowing inlining of objects
graal.YoungPLABSize = 4096                                                  [Long]
          Size of young gen promotion LAB's (in HeapWords)
graal.ZapStackOnMethodEntry = false                                      [Boolean]
graal.ZeroTLAB = false                                                   [Boolean]
          Zero out the newly created TLAB

C:\Games\PolyMC-Windows-Portable-1.4.0\graalvm-ee-java17-22.2.0\bin>
