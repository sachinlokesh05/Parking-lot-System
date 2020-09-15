> db.docs.find({first_name:/el/i}).explain("executionStats")
{
	"queryPlanner" : {
		"plannerVersion" : 1,
		"namespace" : "test.docs",
		"indexFilterSet" : false,
		"parsedQuery" : {
			"first_name" : {
				"$regex" : "el",
				"$options" : "i"
			}
		},
		"winningPlan" : {
			"stage" : "COLLSCAN", /* coluum scanning */
			"filter" : {
				"first_name" : {
					"$regex" : "el",
					"$options" : "i"
				}
			},
			"direction" : "forward"
		},
		"rejectedPlans" : [ ]
	},
	"executionStats" : {
		"executionSuccess" : true,
		"nReturned" : 78,
		"executionTimeMillis" : 2,
		"totalKeysExamined" : 0, /* indexed keys */
		"totalDocsExamined" : 1000,
		"executionStages" : {
			"stage" : "COLLSCAN",
			"filter" : {
				"first_name" : {
					"$regex" : "el",
					"$options" : "i"
				}
			},
			"nReturned" : 78,
			"executionTimeMillisEstimate" : 0, /* time stamp of executation */
			"works" : 1002,
			"advanced" : 78,
			"needTime" : 923,
			"needYield" : 0,
			"saveState" : 7,
			"restoreState" : 7,
			"isEOF" : 1,
			"invalidates" : 0,
			"direction" : "forward",
			"docsExamined" : 1000
		}
	},
	"serverInfo" : {
		"host" : "admin123-Vostro-3580",
		"port" : 27017,
		"version" : "3.6.3",
		"gitVersion" : "9586e557d54ef70f9ca4b43c26892cd55257e1a5"
	},
	"ok" : 1
}
> db.docs.find({first_name:/abcd/i}).explain("executionStats")
{
	"queryPlanner" : {
		"plannerVersion" : 1,
		"namespace" : "test.docs",
		"indexFilterSet" : false,
		"parsedQuery" : {
			"first_name" : {
				"$regex" : "abcd",
				"$options" : "i"
			}
		},
		"winningPlan" : {
			"stage" : "COLLSCAN",
			"filter" : {
				"first_name" : {
					"$regex" : "abcd",
					"$options" : "i"
				}
			},
			"direction" : "forward"
		},
		"rejectedPlans" : [ ]
	},
	"executionStats" : {
		"executionSuccess" : true,
		"nReturned" : 0,
		"executionTimeMillis" : 1,
		"totalKeysExamined" : 0,
		"totalDocsExamined" : 1000,
		"executionStages" : {
			"stage" : "COLLSCAN",
			"filter" : {
				"first_name" : {
					"$regex" : "abcd",
					"$options" : "i"
				}
			},
			"nReturned" : 0,
			"executionTimeMillisEstimate" : 0,
			"works" : 1002,
			"advanced" : 0,
			"needTime" : 1001,
			"needYield" : 0,
			"saveState" : 7,
			"restoreState" : 7,
			"isEOF" : 1,
			"invalidates" : 0,
			"direction" : "forward",
			"docsExamined" : 1000
		}
	},
	"serverInfo" : {
		"host" : "admin123-Vostro-3580",
		"port" : 27017,
		"version" : "3.6.3",
		"gitVersion" : "9586e557d54ef70f9ca4b43c26892cd55257e1a5"
	},
	"ok" : 1
}
> db.docs.find({gender:"Male"}).explain("executionStats")
{
	"queryPlanner" : {
		"plannerVersion" : 1,
		"namespace" : "test.docs",
		"indexFilterSet" : false,
		"parsedQuery" : {
			"gender" : {
				"$eq" : "Male"
			}
		},
		"winningPlan" : {
			"stage" : "FETCH",
			"inputStage" : {
				"stage" : "IXSCAN", /* Index scanning */
				"keyPattern" : {
					"gender" : 1
				},
				"indexName" : "gender_1",
				"isMultiKey" : false,
				"multiKeyPaths" : {
					"gender" : [ ]
				},
				"isUnique" : false,
				"isSparse" : false,
				"isPartial" : false,
				"indexVersion" : 2,
				"direction" : "forward",
				"indexBounds" : {
					"gender" : [
						"[\"Male\", \"Male\"]"
					]
				}
			}
		},
		"rejectedPlans" : [ ]
	},
	"executionStats" : {
		"executionSuccess" : true,
		"nReturned" : 484,
		"executionTimeMillis" : 1,
		"totalKeysExamined" : 484, /* indexed ket examined */
		"totalDocsExamined" : 484, /* same documents returned */
		"executionStages" : {
			"stage" : "FETCH",
			"nReturned" : 484,
			"executionTimeMillisEstimate" : 0, /* time stamp of executation (Comparatively less the column scanning) */
			"works" : 485,
			"advanced" : 484,
			"needTime" : 0,
			"needYield" : 0,
			"saveState" : 3,
			"restoreState" : 3,
			"isEOF" : 1,
			"invalidates" : 0,
			"docsExamined" : 484,
			"alreadyHasObj" : 0,
			"inputStage" : {
				"stage" : "IXSCAN",
				"nReturned" : 484,
				"executionTimeMillisEstimate" : 0,
				"works" : 485,
				"advanced" : 484,
				"needTime" : 0,
				"needYield" : 0,
				"saveState" : 3,
				"restoreState" : 3,
				"isEOF" : 1,
				"invalidates" : 0,
				"keyPattern" : {
					"gender" : 1
				},
				"indexName" : "gender_1",
				"isMultiKey" : false,
				"multiKeyPaths" : {
					"gender" : [ ]
				},
				"isUnique" : false,
				"isSparse" : false,
				"isPartial" : false,
				"indexVersion" : 2,
				"direction" : "forward",
				"indexBounds" : {
					"gender" : [
						"[\"Male\", \"Male\"]"
					]
				},
				"keysExamined" : 484,
				"seeks" : 1,
				"dupsTested" : 0,
				"dupsDropped" : 0,
				"seenInvalidated" : 0
			}
		}
	},
	"serverInfo" : {
		"host" : "admin123-Vostro-3580",
		"port" : 27017,
		"version" : "3.6.3",
		"gitVersion" : "9586e557d54ef70f9ca4b43c26892cd55257e1a5"
	},
	"ok" : 1
}
> db.docs.find({first_name:/abcd/i}).explain("executionStats")
{
	"queryPlanner" : {
		"plannerVersion" : 1,
		"namespace" : "test.docs",
		"indexFilterSet" : false,
		"parsedQuery" : {
			"first_name" : {
				"$regex" : "abcd",
				"$options" : "i"
			}
		},
		"winningPlan" : {
			"stage" : "COLLSCAN",
			"filter" : {
				"first_name" : {
					"$regex" : "abcd",
					"$options" : "i"
				}
			},
			"direction" : "forward"
		},
		"rejectedPlans" : [ ]
	},
	"executionStats" : {
		"executionSuccess" : true,
		"nReturned" : 0,
		"executionTimeMillis" : 1,
		"totalKeysExamined" : 0,
		"totalDocsExamined" : 1000,
		"executionStages" : {
			"stage" : "COLLSCAN",
			"filter" : {
				"first_name" : {
					"$regex" : "abcd",
					"$options" : "i"
				}
			},
			"nReturned" : 0,
			"executionTimeMillisEstimate" : 0,
			"works" : 1002,
			"advanced" : 0,
			"needTime" : 1001,
			"needYield" : 0,
			"saveState" : 7,
			"restoreState" : 7,
			"isEOF" : 1,
			"invalidates" : 0,
			"direction" : "forward",
			"docsExamined" : 1000
		}
	},
	"serverInfo" : {
		"host" : "admin123-Vostro-3580",
		"port" : 27017,
		"version" : "3.6.3",
		"gitVersion" : "9586e557d54ef70f9ca4b43c26892cd55257e1a5"
	},
	"ok" : 1
}
> db.docs.find({gender:"Male"}).explain("executionStats")
{
	"queryPlanner" : {
		"plannerVersion" : 1,
		"namespace" : "test.docs",
		"indexFilterSet" : false,
		"parsedQuery" : {
			"gender" : {
				"$eq" : "Male"
			}
		},
		"winningPlan" : {
			"stage" : "FETCH",
			"inputStage" : {
				"stage" : "IXSCAN",
				"keyPattern" : {
					"gender" : 1
				},
				"indexName" : "gender_1",
				"isMultiKey" : false,
				"multiKeyPaths" : {
					"gender" : [ ]
				},
				"isUnique" : false,
				"isSparse" : false,
				"isPartial" : false,
				"indexVersion" : 2,
				"direction" : "forward",
				"indexBounds" : {
					"gender" : [
						"[\"Male\", \"Male\"]"
					]
				}
			}
		},
		"rejectedPlans" : [ ]
	},
	"executionStats" : {
		"executionSuccess" : true,
		"nReturned" : 484,
		"executionTimeMillis" : 1,
		"totalKeysExamined" : 484,
		"totalDocsExamined" : 484,
		"executionStages" : {
			"stage" : "FETCH",
			"nReturned" : 484,
			"executionTimeMillisEstimate" : 0,
			"works" : 485,
			"advanced" : 484,
			"needTime" : 0,
			"needYield" : 0,
			"saveState" : 3,
			"restoreState" : 3,
			"isEOF" : 1,
			"invalidates" : 0,
			"docsExamined" : 484,
			"alreadyHasObj" : 0,
			"inputStage" : {
				"stage" : "IXSCAN",
				"nReturned" : 484,
				"executionTimeMillisEstimate" : 0,
				"works" : 485,
				"advanced" : 484,
				"needTime" : 0,
				"needYield" : 0,
				"saveState" : 3,
				"restoreState" : 3,
				"isEOF" : 1,
				"invalidates" : 0,
				"keyPattern" : {
					"gender" : 1
				},
				"indexName" : "gender_1",
				"isMultiKey" : false,
				"multiKeyPaths" : {
					"gender" : [ ]
				},
				"isUnique" : false,
				"isSparse" : false,
				"isPartial" : false,
				"indexVersion" : 2,
				"direction" : "forward",
				"indexBounds" : {
					"gender" : [
						"[\"Male\", \"Male\"]"
					]
				},
				"keysExamined" : 484,
				"seeks" : 1,
				"dupsTested" : 0,
				"dupsDropped" : 0,
				"seenInvalidated" : 0
			}
		}
	},
	"serverInfo" : {
		"host" : "admin123-Vostro-3580",
		"port" : 27017,
		"version" : "3.6.3",
		"gitVersion" : "9586e557d54ef70f9ca4b43c26892cd55257e1a5"
	},
	"ok" : 1
}
